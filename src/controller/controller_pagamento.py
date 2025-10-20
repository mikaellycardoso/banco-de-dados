from model.Pagamento import Pagamento
from model.Reserva import Reserva
from conexion.oracle_queries import OracleQueries
from datetime import date
import decimal

class Controller_Pagamento:
    def __init__(self):
        pass

    def inserir_pagamento(self) -> Pagamento:
        """
        Insere um novo pagamento no banco de dados.
        Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks
        """

        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursor para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída para o ID do pagamento
        output_value = cursor.var(int)

        # Solicita os dados do pagamento ao usuário
        id_reserva = int(input("ID da Reserva: "))
        valor_pago = decimal.Decimal(input("Valor Pago: "))
        data_pagamento = input("Data do Pagamento (AAAA-MM-DD): ")
        data_pagamento = date.fromisoformat(data_pagamento)
        metodo = input("Método de Pagamento: ")
        status = input("Status do Pagamento: ")

        # Cria o dicionário de dados para o PL/SQL
        data = dict(
            id_pagamento=output_value,
            id_reserva=id_reserva,
            valor_pago=valor_pago,
            data_pagamento=data_pagamento,
            metodo=metodo,
            status=status
        )

        # Executa o bloco PL/SQL para inserir o pagamento
        cursor.execute("""
        begin
            :id_pagamento := PAGAMENTOS_ID_PAGAMENTO_SEQ.NEXTVAL;
            insert into pagamentos (id_pagamento, id_reserva, valor_pago, data_pagamento, metodo, status)
            values(:id_pagamento, :id_reserva, :valor_pago, :data_pagamento, :metodo, :status);
        end;
        """, data)

        # Recupera o ID do pagamento inserido
        id_pagamento = output_value.getvalue()
        # Confirma a inserção no banco
        oracle.conn.commit()

        # Recupera os dados do pagamento inserido
        df_pagamento = oracle.sqlToDataFrame(
            f"select * from pagamentos where id_pagamento = {id_pagamento}"
        )

        # Cria o objeto Pagamento
        novo_pagamento = Pagamento(
            df_pagamento.id_pagamento.values[0],
            df_pagamento.id_reserva.values[0],
            df_pagamento.valor_pago.values[0],
            df_pagamento.data_pagamento.values[0],
            df_pagamento.metodo.values[0],
            df_pagamento.status.values[0]
        )

        # Exibe os atributos do pagamento criado
        print(novo_pagamento.to_string())
        return novo_pagamento

    def atualizar_pagamento(self) -> Pagamento:
        """
        Atualiza um pagamento existente.
        """

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita o ID do pagamento que será alterado
        id_pagamento = int(input("ID do Pagamento que irá alterar: "))

        # Verifica se o pagamento existe
        if not self.verifica_existencia_pagamento(oracle, id_pagamento):

            # Solicita novos dados
            valor_pago = decimal.Decimal(input("Novo Valor Pago: "))
            data_pagamento = input("Nova Data do Pagamento (AAAA-MM-DD): ")
            data_pagamento = date.fromisoformat(data_pagamento)
            metodo = input("Novo Método de Pagamento: ")
            status = input("Novo Status do Pagamento: ")

            # Atualiza o pagamento no banco
            oracle.write(f"""
                update pagamentos
                set valor_pago = {valor_pago}, data_pagamento = '{data_pagamento}', metodo = '{metodo}', status = '{status}'
                where id_pagamento = {id_pagamento}
            """)

            # Recupera os dados atualizados
            df_pagamento = oracle.sqlToDataFrame(
                f"select * from pagamentos where id_pagamento = {id_pagamento}"
            )

            # Cria objeto Pagamento atualizado
            pagamento_atualizado = Pagamento(
                df_pagamento.id_pagamento.values[0],
                df_pagamento.id_reserva.values[0],
                df_pagamento.valor_pago.values[0],
                df_pagamento.data_pagamento.values[0],
                df_pagamento.metodo.values[0],
                df_pagamento.status.values[0]
            )

            print(pagamento_atualizado.to_string())
            return pagamento_atualizado

        else:
            print(f"O pagamento ID {id_pagamento} não existe.")
            return None

    def excluir_pagamento(self):
        """
        Exclui um pagamento do banco de dados.
        """

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_pagamento = int(input("ID do Pagamento que irá excluir: "))

        if not self.verifica_existencia_pagamento(oracle, id_pagamento):

            # Recupera os dados antes de excluir
            df_pagamento = oracle.sqlToDataFrame(
                f"select * from pagamentos where id_pagamento = {id_pagamento}"
            )

            # Remove o pagamento
            oracle.write(f"delete from pagamentos where id_pagamento = {id_pagamento}")

            # Cria objeto para informar que foi removido
            pagamento_excluido = Pagamento(
                df_pagamento.id_pagamento.values[0],
                df_pagamento.id_reserva.values[0],
                df_pagamento.valor_pago.values[0],
                df_pagamento.data_pagamento.values[0],
                df_pagamento.metodo.values[0],
                df_pagamento.status.values[0]
            )

            print("Pagamento Removido com Sucesso!")
            print(pagamento_excluido.to_string())

        else:
            print(f"O pagamento ID {id_pagamento} não existe.")

    def verifica_existencia_pagamento(self, oracle: OracleQueries, id_pagamento: int = None) -> bool:
        """
        Verifica se o pagamento existe no banco.
        Retorna True se não existe, False se existe.
        """
        df_pagamento = oracle.sqlToDataFrame(
            f"select id_pagamento from pagamentos where id_pagamento = {id_pagamento}"
        )
        return df_pagamento.empty
