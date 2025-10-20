from model.Hospede import Hospede
from conexion.oracle_queries import OracleQueries

class Controller_Hospede:
    def __init__(self):
        pass

    def inserir_hospede(self) -> Hospede:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CPF
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_hospede(oracle, cpf):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            email = input("email (Novo): ")
            telefone = input("telefone (Novo): ")

            # Insere e persiste o novo hospede
            oracle.write(f"insert into hospede values ('{cpf}', '{nome}','{email}','{telefone}')")

            # Recupera os dados do novo hospede criado transformando em um DataFrame
            df_hospede = oracle.sqlToDataFrame(f"select cpf, nome from hospede where cpf = '{cpf}'")

            # Cria um novo objeto hospede
            novo_hospede = Hospede (
                df_hospede.cpf.values[0],
                df_hospede.nome.values[0],
                df_hospede.email.values[0],
                df_hospede.telefone.values[0]
)

            # Exibe os atributos do novo hospede
            print(novo_hospede.to_string())

            # Retorna o objeto novo_hospede para utilização posterior, caso necessário
            return novo_hospede
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_hospede(self) -> Hospede:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do cliente a ser alterado
        cpf = int(input("CPF do hospede que deseja alterar o nome: "))

        # Verifica se o hospede existe na base de dados
        if not self.verifica_existencia_hospede(oracle, cpf):

            # Solicita a nova descrição do hospede
            novo_nome = input("Nome (Novo): ")

            # Atualiza o nome do hospede existente
            oracle.write(f"update hospede set nome = '{novo_nome}' where cpf = {cpf}")

            # Recupera os dados do novo hospede criado transformando em um DataFrame
            df_hospede = oracle.sqlToDataFrame(f"select cpf, nome from hospede where cpf = {cpf}")

            # Cria um novo objeto hospede
            hospede_atualizado = Hospede (df_hospede.cpf.values[0], 
                                          df_hospede.nome.values[0], 
                                          df_hospede.email.values[0], 
                                          df_hospede.telefone.values[0])

            # Exibe os atributos do novo hospede
            print(hospede_atualizado.to_string())

            # Retorna o objeto hospede_atualizado para utilização posterior, caso necessário
            return hospede_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_hospede(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do hospede a ser alterado
        cpf = int(input("CPF do Hospede que irá excluir: "))

        # Verifica se o hospede existe na base de dados
        if not self.verifica_existencia_hospede(oracle, cpf):

            # Recupera os dados do novo hospede criado transformando em um DataFrame
            df_hospede = oracle.sqlToDataFrame(f"select cpf, nome from hospede where cpf = {cpf}")

            # Revome o hospede da tabela
            oracle.write(f"delete from hospede where cpf = {cpf}")

            # Cria um novo objeto hospede para informar que foi removido
            hospede_excluido = Hospede(df_hospede.cpf.values[0], df_hospede.nome.values[0], df_hospede.email.values[0], df_hospede.telefone.values[0])

            # Exibe os atributos do hospede excluído
            print("Hospede Removido com Sucesso!")
            print(hospede_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_hospede(self, oracle:OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do novo hospede criado transformando em um DataFrame
        df_hospede = oracle.sqlToDataFrame(f"select cpf, nome from hospede where cpf = {cpf}")
        return df_hospede.empty
