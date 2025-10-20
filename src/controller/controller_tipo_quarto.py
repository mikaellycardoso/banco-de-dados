from model.tipo_quarto import tipo_quarto
from conexion.oracle_queries import OracleQueries
import decimal

class Controller_TipoQuarto:
    def __init__(self):
        pass

    def inserir_tipo_quarto(self) -> tipo_quarto:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursor para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado (para capturar o ID gerado pela sequence)
        output_value = cursor.var(int)

        # Solicita ao usuário os novos dados do tipo de quarto
        nome_tipo = input("Nome do Tipo de Quarto (Novo): ")
        descricao_tipo = input("Descrição (Nova): ")
        capacidade_maxima = int(input("Capacidade Máxima (Nova): "))
        preco_diaria = decimal.Decimal(input("Preço da Diária (Novo): "))

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(
            id_tipo_quarto=output_value,
            nome_tipo=nome_tipo,
            descricao_tipo=descricao_tipo,
            capacidade_maxima=capacidade_maxima,
            preco_diaria=preco_diaria
        )

        # Executa o bloco PL/SQL anônimo para inserção do novo tipo de quarto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :id_tipo_quarto := TIPO_QUARTO_ID_SEQ.NEXTVAL;
            insert into tipo_quarto values(:id_tipo_quarto, :nome_tipo, :descricao_tipo, :capacidade_maxima, :preco_diaria);
        end;
        """, data)

        # Recupera o ID do novo tipo de quarto
        id_tipo_quarto = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo tipo de quarto criado transformando em um DataFrame
        df_tipo = oracle.sqlToDataFrame(f"""
            select id_tipo_quarto, nome_tipo, descricao_tipo, capacidade_maxima, preco_diaria 
            from tipo_quarto 
            where id_tipo_quarto = {id_tipo_quarto}
        """)
        # Cria um novo objeto tipo_quarto
        novo_tipo = tipo_quarto(df_tipo.id_tipo_quarto.values[0],
                                df_tipo.nome_tipo.values[0],
                                df_tipo.descricao_tipo.values[0],
                                df_tipo.capacidade_maxima.values[0],
                                df_tipo.preco_diaria.values[0])
        # Exibe os atributos do novo tipo de quarto
        print(novo_tipo.to_string())
        # Retorna o objeto novo_tipo para utilização posterior, caso necessário
        return novo_tipo

    def atualizar_tipo_quarto(self) -> tipo_quarto:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o ID do tipo de quarto a ser alterado
        id_tipo_quarto = int(input("ID do Tipo de Quarto que irá alterar: "))

        # Verifica se o tipo de quarto existe na base de dados
        if not self.verifica_existencia_tipo_quarto(oracle, id_tipo_quarto):
            # Solicita os novos dados
            nome_tipo = input("Nome do Tipo de Quarto (Novo): ")
            descricao_tipo = input("Descrição (Nova): ")
            capacidade_maxima = int(input("Capacidade Máxima (Nova): "))
            preco_diaria = decimal.Decimal(input("Preço da Diária (Novo): "))

            # Atualiza o tipo de quarto existente
            oracle.write(f"""
                update tipo_quarto 
                set nome_tipo = '{nome_tipo}', descricao_tipo = '{descricao_tipo}', 
                    capacidade_maxima = {capacidade_maxima}, preco_diaria = {preco_diaria}
                where id_tipo_quarto = {id_tipo_quarto}
            """)

            # Recupera os dados do tipo de quarto atualizado
            df_tipo = oracle.sqlToDataFrame(f"""
                select id_tipo_quarto, nome_tipo, descricao_tipo, capacidade_maxima, preco_diaria 
                from tipo_quarto 
                where id_tipo_quarto = {id_tipo_quarto}
            """)
            # Cria um novo objeto tipo_quarto com os dados atualizados
            tipo_atualizado = tipo_quarto(df_tipo.id_tipo_quarto.values[0],
                                          df_tipo.nome_tipo.values[0],
                                          df_tipo.descricao_tipo.values[0],
                                          df_tipo.capacidade_maxima.values[0],
                                          df_tipo.preco_diaria.values[0])
            # Exibe os atributos atualizados
            print(tipo_atualizado.to_string())
            # Retorna o objeto atualizado para uso posterior
            return tipo_atualizado
        else:
            print(f"O tipo de quarto ID {id_tipo_quarto} não existe.")
            return None

    def excluir_tipo_quarto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o ID do tipo de quarto a ser excluído
        id_tipo_quarto = int(input("ID do Tipo de Quarto que irá excluir: "))

        # Verifica se o tipo de quarto existe na base de dados
        if not self.verifica_existencia_tipo_quarto(oracle, id_tipo_quarto):
            # Recupera os dados do tipo de quarto antes da exclusão
            df_tipo = oracle.sqlToDataFrame(f"""
                select id_tipo_quarto, nome_tipo, descricao_tipo, capacidade_maxima, preco_diaria 
                from tipo_quarto 
                where id_tipo_quarto = {id_tipo_quarto}
            """)
            # Remove o tipo de quarto da tabela
            oracle.write(f"delete from tipo_quarto where id_tipo_quarto = {id_tipo_quarto}")
            # Cria um objeto tipo_quarto para mostrar os dados removidos
            tipo_excluido = tipo_quarto(df_tipo.id_tipo_quarto.values[0],
                                        df_tipo.nome_tipo.values[0],
                                        df_tipo.descricao_tipo.values[0],
                                        df_tipo.capacidade_maxima.values[0],
                                        df_tipo.preco_diaria.values[0])
            # Exibe mensagem de sucesso e os dados excluídos
            print("Tipo de Quarto Removido com Sucesso!")
            print(tipo_excluido.to_string())
        else:
            print(f"O tipo de quarto ID {id_tipo_quarto} não existe.")

    def verifica_existencia_tipo_quarto(self, oracle:OracleQueries, id_tipo_quarto:int=None) -> bool:
        # Recupera o tipo de quarto a partir do ID informado
        df_tipo = oracle.sqlToDataFrame(f"select id_tipo_quarto from tipo_quarto where id_tipo_quarto = {id_tipo_quarto}")
        # Retorna True se não houver resultados, indicando que o registro não existe
        return df_tipo.empty
