from model.Quarto import Quarto
from model.tipo_quarto import tipo_quarto
from conexion.oracle_queries import OracleQueries

class Controller_Quarto:
    def __init__(self):
        pass

    def inserir_quarto(self) -> Quarto:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursor para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída (para capturar o ID do quarto gerado pela sequence)
        output_value = cursor.var(int)

        # Solicita ao usuário os dados do quarto
        numero_quarto = int(input("Número do Quarto (Novo): "))
        andar_quarto = int(input("Andar do Quarto (Novo): "))
        id_tipo_quarto = int(input("ID do Tipo de Quarto: "))
        status = input("Status do Quarto (Novo): ")

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(
            id_quarto=output_value,
            numero_quarto=numero_quarto,
            andar_quarto=andar_quarto,
            id_tipo_quarto=id_tipo_quarto,
            status=status
        )

        # Executa o bloco PL/SQL anônimo para inserção do novo quarto
        cursor.execute("""
        begin
            :id_quarto := QUARTO_ID_SEQ.NEXTVAL;
            insert into quarto values(:id_quarto, :numero_quarto, :andar_quarto, :id_tipo_quarto, :status);
        end;
        """, data)

        # Recupera o ID do novo quarto
        id_quarto = output_value.getvalue()
        # Persiste as alterações
        oracle.conn.commit()
        # Recupera os dados do novo quarto criado (com join na tabela tipo_quarto)
        df_quarto = oracle.sqlToDataFrame(f"""
            select q.id_quarto, q.numero_quarto, q.andar_quarto, q.status,
                   tq.id_tipo_quarto, tq.nome_tipo, tq.descricao_tipo, tq.capacidade_maxima, tq.preco_diaria
            from quarto q
            inner join tipo_quarto tq on q.id_tipo_quarto = tq.id_tipo_quarto
            where q.id_quarto = {id_quarto}
        """)

        # Cria um objeto tipo_quarto associado
        tipo = tipo_quarto(df_quarto.id_tipo_quarto.values[0],
                           df_quarto.nome_tipo.values[0],
                           df_quarto.descricao_tipo.values[0],
                           df_quarto.capacidade_maxima.values[0],
                           df_quarto.preco_diaria.values[0])
        # Cria o objeto Quarto
        novo_quarto = Quarto(df_quarto.id_quarto.values[0],
                             df_quarto.numero_quarto.values[0],
                             df_quarto.andar_quarto.values[0],
                             tipo,
                             df_quarto.status.values[0])
        # Exibe os atributos do novo quarto
        print(novo_quarto.to_string())
        # Retorna o objeto novo_quarto
        return novo_quarto

    def atualizar_quarto(self) -> Quarto:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o ID do quarto a ser alterado
        id_quarto = int(input("ID do Quarto que irá alterar: "))

        # Verifica se o quarto existe na base de dados
        if not self.verifica_existencia_quarto(oracle, id_quarto):
            # Solicita os novos dados do quarto
            numero_quarto = int(input("Número do Quarto (Novo): "))
            andar_quarto = int(input("Andar (Novo): "))
            id_tipo_quarto = int(input("ID do Tipo de Quarto (Novo): "))
            status = input("Status (Novo): ")

            # Atualiza o quarto existente
            oracle.write(f"""
                update quarto 
                set numero_quarto = {numero_quarto}, andar_quarto = {andar_quarto}, 
                    id_tipo_quarto = {id_tipo_quarto}, status = '{status}'
                where id_quarto = {id_quarto}
            """)

            # Recupera os dados do quarto atualizado
            df_quarto = oracle.sqlToDataFrame(f"""
                select q.id_quarto, q.numero_quarto, q.andar_quarto, q.status,
                       tq.id_tipo_quarto, tq.nome_tipo, tq.descricao_tipo, tq.capacidade_maxima, tq.preco_diaria
                from quarto q
                inner join tipo_quarto tq on q.id_tipo_quarto = tq.id_tipo_quarto
                where q.id_quarto = {id_quarto}
            """)

            # Cria o objeto tipo_quarto atualizado
            tipo = tipo_quarto(df_quarto.id_tipo_quarto.values[0],
                               df_quarto.nome_tipo.values[0],
                               df_quarto.descricao_tipo.values[0],
                               df_quarto.capacidade_maxima.values[0],
                               df_quarto.preco_diaria.values[0])
            # Cria o objeto quarto atualizado
            quarto_atualizado = Quarto(df_quarto.id_quarto.values[0],
                                       df_quarto.numero_quarto.values[0],
                                       df_quarto.andar_quarto.values[0],
                                       tipo,
                                       df_quarto.status.values[0])
            # Exibe os atributos do quarto atualizado
            print(quarto_atualizado.to_string())
            # Retorna o objeto atualizado
            return quarto_atualizado
        else:
            print(f"O quarto ID {id_quarto} não existe.")
            return None

    def excluir_quarto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita o ID do quarto a ser excluído
        id_quarto = int(input("ID do Quarto que irá excluir: "))

        # Verifica se o quarto existe na base de dados
        if not self.verifica_existencia_quarto(oracle, id_quarto):
            # Recupera os dados do quarto antes da exclusão
            df_quarto = oracle.sqlToDataFrame(f"""
                select q.id_quarto, q.numero_quarto, q.andar_quarto, q.status,
                       tq.id_tipo_quarto, tq.nome_tipo, tq.descricao_tipo, tq.capacidade_maxima, tq.preco_diaria
                from quarto q
                inner join tipo_quarto tq on q.id_tipo_quarto = tq.id_tipo_quarto
                where q.id_quarto = {id_quarto}
            """)
            # Remove o quarto da tabela
            oracle.write(f"delete from quarto where id_quarto = {id_quarto}")

            # Cria objetos representando o quarto excluído
            tipo = tipo_quarto(df_quarto.id_tipo_quarto.values[0],
                               df_quarto.nome_tipo.values[0],
                               df_quarto.descricao_tipo.values[0],
                               df_quarto.capacidade_maxima.values[0],
                               df_quarto.preco_diaria.values[0])
            quarto_excluido = Quarto(df_quarto.id_quarto.values[0],
                                     df_quarto.numero_quarto.values[0],
                                     df_quarto.andar_quarto.values[0],
                                     tipo,
                                     df_quarto.status.values[0])
            # Exibe mensagem de sucesso e os dados excluídos
            print("Quarto Removido com Sucesso!")
            print(quarto_excluido.to_string())
        else:
            print(f"O quarto ID {id_quarto} não existe.")

    def verifica_existencia_quarto(self, oracle:OracleQueries, id_quarto:int=None) -> bool:
        # Recupera o quarto a partir do ID informado
        df_quarto = oracle.sqlToDataFrame(f"select id_quarto from quarto where id_quarto = {id_quarto}")
        # Retorna True se o DataFrame estiver vazio (não existe)
        return df_quarto.empty
