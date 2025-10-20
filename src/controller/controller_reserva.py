from model.Reserva import Reserva
from conexion.oracle_queries import OracleQueries

class Controller_Reserva:
    def __init__(self):
        pass

    def inserir_reserva(self) -> Reserva:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        # Cria uma nova conexão com o banco
        oracle = OracleQueries()

        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()

        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Solicita ao usuario os dados da nova reserva
        data_checkin = input("Data de Check-in (AAAA-MM-DD): ")
        data_checkout = input("Data de Check-out (AAAA-MM-DD): ")
        valor_total = input("Valor Total: ")
        cpf_hospede = input("CPF do Hóspede: ")
        numero_quarto = input("Número do Quarto: ")

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(
            codigo=output_value,
            data_checkin=data_checkin,
            data_checkout=data_checkout,
            valor_total=valor_total,
            cpf_hospede=cpf_hospede,
            numero_quarto=numero_quarto
        )

        # Executa o bloco PL/SQL anônimo para inserção da nova reserva e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := RESERVA_ID_RESERVA_SEQ.NEXTVAL;
            insert into reserva values(:codigo, TO_DATE(:data_checkin,'YYYY-MM-DD'), TO_DATE(:data_checkout,'YYYY-MM-DD'), :valor_total, :cpf_hospede, :numero_quarto);
        end;
        """, data)

        # Recupera o código da nova reserva
        id_reserva = output_value.getvalue()

        # Persiste (confirma) as alterações
        oracle.conn.commit()

        # Recupera os dados da nova reserva criada transformando em um DataFrame
        df_reserva = oracle.sqlToDataFrame(f"select id_reserva, data_checkin, data_checkout, valor_total, cpf_hospede, numero_quarto from reserva where id_reserva = {id_reserva}")

        # Cria um novo objeto Reserva
        nova_reserva = Reserva(
            df_reserva.id_reserva.values[0],
            df_reserva.data_checkin.values[0],
            df_reserva.data_checkout.values[0],
            df_reserva.valor_total.values[0],
            df_reserva.cpf_hospede.values[0],
            df_reserva.numero_quarto.values[0]
        )
        # Exibe os atributos da nova reserva
        print(nova_reserva.to_string())

        # Retorna o objeto nova_reserva para utilização posterior, caso necessário
        return nova_reserva

    def atualizar_reserva(self) -> Reserva:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da reserva a ser alterado
        id_reserva = int(input("Código da Reserva que irá alterar: "))

        # Verifica se a reserva existe na base de dados
        if not self.verifica_existencia_reserva(oracle, id_reserva):

            # Solicita o novo valor total da reserva
            novo_valor = input("Novo Valor Total: ")

            # Atualiza o valor da reserva existente
            oracle.write(f"update reserva set valor_total = {novo_valor} where id_reserva = {id_reserva}")

            # Recupera os dados da reserva alterada transformando em um DataFrame
            df_reserva = oracle.sqlToDataFrame(f"select id_reserva, data_checkin, data_checkout, valor_total, cpf_hospede, numero_quarto from reserva where id_reserva = {id_reserva}")
            # Cria um novo objeto Reserva
            reserva_atualizada = Reserva(
                df_reserva.id_reserva.values[0],
                df_reserva.data_checkin.values[0],
                df_reserva.data_checkout.values[0],
                df_reserva.valor_total.values[0],
                df_reserva.cpf_hospede.values[0],
                df_reserva.numero_quarto.values[0]
            )
            # Exibe os atributos da reserva alterada
            print(reserva_atualizada.to_string())
            # Retorna o objeto reserva_atualizada
            return reserva_atualizada
        else:
            print(f"O código {id_reserva} não existe.")
            return None

    def excluir_reserva(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da reserva a ser excluída
        id_reserva = int(input("Código da Reserva que irá excluir: "))

        # Verifica se a reserva existe na base de dados
        if not self.verifica_existencia_reserva(oracle, id_reserva):

            # Recupera os dados da reserva transformando em um DataFrame
            df_reserva = oracle.sqlToDataFrame(f"select id_reserva, data_checkin, data_checkout, valor_total, cpf_hospede, numero_quarto from reserva where id_reserva = {id_reserva}")

            # Revome a reserva da tabela
            oracle.write(f"delete from reserva where id_reserva = {id_reserva}")
            # Cria um novo objeto Reserva para informar que foi removido
            reserva_excluida = Reserva(
                df_reserva.id_reserva.values[0],df_reserva.data_checkin.values[0],df_reserva.data_checkout.values[0], df_reserva.valor_total.values[0],
                df_reserva.cpf_hospede.values[0],
                df_reserva.numero_quarto.values[0]
            )
            # Exibe os atributos da reserva excluída
            print("Reserva Removida com Sucesso!")
            print(reserva_excluida.to_string())
        else:
            print(f"O código {id_reserva} não existe.")

    def verifica_existencia_reserva(self, oracle:OracleQueries, id_reserva:int=None) -> bool:
        # Recupera os dados da reserva transformando em um DataFrame
        df_reserva = oracle.sqlToDataFrame(f"select id_reserva from reserva where id_reserva = {id_reserva}")
        return df_reserva.empty
