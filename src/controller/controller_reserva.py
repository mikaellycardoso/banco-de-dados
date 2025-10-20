from model.Reserva import Reserva
from conexion.oracle_queries import OracleQueries
import decimal
from datetime import date

class Controller_Reserva:
    def __init__(self):
        pass
    
    def verifica_existencia_hospede_quarto(self, oracle: OracleQueries, cpf_hospede: str, numero_quarto: str):
        
        df_hospede = oracle.sqlToDataFrame(f"select id_hospede from hospede where documento = '{cpf_hospede}'")
        if df_hospede.empty:
            print(f"ERRO: Hóspede com CPF {cpf_hospede} não encontrado.")
            return None, None
        id_hospede = df_hospede.id_hospede.values[0]

        df_quarto = oracle.sqlToDataFrame(f"select id_quarto from quarto where numero_quarto = '{numero_quarto}'")
        if df_quarto.empty:
            print(f"ERRO: Quarto com número {numero_quarto} não encontrado.")
            return None, None
        id_quarto = df_quarto.id_quarto.values[0]

        return id_hospede, id_quarto


    def inserir_reserva(self) -> Reserva:
        oracle = OracleQueries(can_write=True)
        cursor = oracle.connect()
        output_value = cursor.var(int)
        
        print("\n--- INSERÇÃO DE NOVA RESERVA ---")
        data_checkin = input("Data de Check-in (AAAA-MM-DD): ")
        data_checkout = input("Data de Check-out (AAAA-MM-DD): ")
        valor_total = input("Valor Total: ")
        quant_hospedes = int(input("Quantidade de Hóspedes: "))
        status = input("Status da Reserva (EX: CONFIRMADA): ")
        
        cpf_hospede = input("CPF do Hóspede: ")
        numero_quarto = input("Número do Quarto: ")
        
        id_hospede, id_quarto = self.verifica_existencia_hospede_quarto(oracle, cpf_hospede, numero_quarto)

        if id_hospede is None or id_quarto is None:
             oracle.close()
             return None

        data = dict(
            codigo=output_value,
            id_hospede=id_hospede,
            id_quarto=id_quarto,
            data_checkin=data_checkin,
            data_checkout=data_checkout,
            quant_hospedes=quant_hospedes,
            status=status,
            valor_total=decimal.Decimal(valor_total)
        )

        cursor.execute("""
        begin
            :codigo := RESERVA_ID_SEQ.NEXTVAL;
            insert into reserva (id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, quant_hospedes, status, valor_total, data_reserva)
            values(:codigo, :id_hospede, :id_quarto, TO_DATE(:data_checkin,'YYYY-MM-DD'), TO_DATE(:data_checkout,'YYYY-MM-DD'), :quant_hospedes, :status, :valor_total, SYSDATE);
        end;
        """, data)

        id_reserva = output_value.getvalue()

        oracle.conn.commit()

        df_reserva = oracle.sqlToDataFrame(f"select id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, valor_total, quant_hospedes, status, data_reserva from reserva where id_reserva = {id_reserva}")
        
        nova_reserva = Reserva(
            df_reserva.id_reserva.values[0],
            df_reserva.id_hospede.values[0],
            df_reserva.id_quarto.values[0],
            df_reserva.data_checkin.values[0],
            df_reserva.data_checkout.values[0],
            df_reserva.data_reserva.values[0],
            df_reserva.valor_total.values[0],
            df_reserva.quant_hospedes.values[0],
            df_reserva.status.values[0]
        )
        
        print(nova_reserva.to_string())

        return nova_reserva


    def atualizar_reserva(self) -> Reserva:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_reserva = int(input("Código da Reserva que irá alterar: "))

        if not self.verifica_existencia_reserva(oracle, id_reserva):
            
            novo_valor = input("Novo Valor Total: ")

            oracle.write(f"update reserva set valor_total = {novo_valor} where id_reserva = {id_reserva}")

            df_reserva = oracle.sqlToDataFrame(f"select id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, valor_total, quant_hospedes, status, data_reserva from reserva where id_reserva = {id_reserva}")
            
            reserva_atualizada = Reserva(
                df_reserva.id_reserva.values[0],
                df_reserva.id_hospede.values[0],
                df_reserva.id_quarto.values[0],
                df_reserva.data_checkin.values[0],
                df_reserva.data_checkout.values[0],
                df_reserva.data_reserva.values[0],
                df_reserva.valor_total.values[0],
                df_reserva.quant_hospedes.values[0],
                df_reserva.status.values[0]
            )
            print(reserva_atualizada.to_string())
            return reserva_atualizada
        else:
            print(f"O código {id_reserva} não existe.")
            return None

    def excluir_reserva(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_reserva = int(input("Código da Reserva que irá excluir: "))

        if not self.verifica_existencia_reserva(oracle, id_reserva):

            df_reserva = oracle.sqlToDataFrame(f"select id_reserva, id_hospede, id_quarto, data_checkin, data_checkout, valor_total, quant_hospedes, status, data_reserva from reserva where id_reserva = {id_reserva}")

            oracle.write(f"delete from reserva where id_reserva = {id_reserva}")
            
            reserva_excluida = Reserva(
                df_reserva.id_reserva.values[0],
                df_reserva.id_hospede.values[0],
                df_reserva.id_quarto.values[0],
                df_reserva.data_checkin.values[0],
                df_reserva.data_checkout.values[0],
                df_reserva.data_reserva.values[0],
                df_reserva.valor_total.values[0],
                df_reserva.quant_hospedes.values[0],
                df_reserva.status.values[0]
            )
            print("Reserva Removida com Sucesso!")
            print(reserva_excluida.to_string())
        else:
            print(f"O código {id_reserva} não existe.")

    def verifica_existencia_reserva(self, oracle:OracleQueries, id_reserva:int=None) -> bool:
        df_reserva = oracle.sqlToDataFrame(f"select id_reserva from reserva where id_reserva = {id_reserva}")
        return df_reserva.empty
