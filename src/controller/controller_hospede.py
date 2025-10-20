from model.Hospede import Hospede
from conexion.oracle_queries import OracleQueries

class Controller_Hospede:
    def __init__(self):
        pass

    def inserir_hospede(self) -> Hospede:
        
        oracle = OracleQueries(can_write=True)
        cursor = oracle.connect()
        output_value = cursor.var(int)
        
        print("\n--- INSERÇÃO DE NOVO HÓSPEDE ---")
        documento = input("Documento/CPF (Novo): ")

        if self.verifica_existencia_hospede(oracle, documento):
            
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")

            data = dict(
                id_hospede=output_value,
                documento=documento,
                nome=nome,
                sobrenome=sobrenome,
                email=email,
                telefone=telefone
            )

            cursor.execute("""
            begin
                :id_hospede := HOSPEDE_ID_SEQ.NEXTVAL;
                insert into hospede (id_hospede, documento, nome, sobrenome, email, telefone, criado_em)
                values(:id_hospede, :documento, :nome, :sobrenome, :email, :telefone, SYSDATE);
            end;
            """, data)
            
            id_hospede = output_value.getvalue()
            oracle.conn.commit()

            df_hospede = oracle.sqlToDataFrame(f"select id_hospede, documento, nome, sobrenome, email, telefone from hospede where id_hospede = {id_hospede}")

            novo_hospede = Hospede (
                df_hospede.id_hospede.values[0],
                df_hospede.documento.values[0],
                df_hospede.nome.values[0],
                df_hospede.sobrenome.values[0],
                df_hospede.email.values[0],
                df_hospede.telefone.values[0]
            )

            print(novo_hospede.to_string())

            return novo_hospede
        else:
            print(f"O Documento/CPF {documento} já está cadastrado.")
            return None

    def atualizar_hospede(self) -> Hospede:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        documento = input("Documento/CPF do hóspede que deseja alterar: ")

        if not self.verifica_existencia_hospede(oracle, documento):
            
            novo_nome = input("Nome (Novo): ")
            novo_sobrenome = input("Sobrenome (Novo): ")
            novo_email = input("Email (Novo): ")
            novo_telefone = input("Telefone (Novo): ")

            oracle.write(f"update hospede set nome = '{novo_nome}', sobrenome = '{novo_sobrenome}', email = '{novo_email}', telefone = '{novo_telefone}' where documento = '{documento}'")

            df_hospede = oracle.sqlToDataFrame(f"select id_hospede, documento, nome, sobrenome, email, telefone from hospede where documento = '{documento}'")

            hospede_atualizado = Hospede (
                df_hospede.id_hospede.values[0], 
                df_hospede.documento.values[0],
                df_hospede.nome.values[0],
                df_hospede.sobrenome.values[0],
                df_hospede.email.values[0], 
                df_hospede.telefone.values[0]
            )

            print(hospede_atualizado.to_string())

            return hospede_atualizado
        else:
            print(f"O Documento/CPF {documento} não existe.")
            return None

    def excluir_hospede(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        documento = input("Documento/CPF do Hóspede que irá excluir: ")

        if not self.verifica_existencia_hospede(oracle, documento):

            df_hospede = oracle.sqlToDataFrame(f"select id_hospede, documento, nome, sobrenome, email, telefone from hospede where documento = '{documento}'")

            oracle.write(f"delete from hospede where documento = '{documento}'")

            hospede_excluido = Hospede(
                df_hospede.id_hospede.values[0], 
                df_hospede.documento.values[0],
                df_hospede.nome.values[0], 
                df_hospede.sobrenome.values[0],
                df_hospede.email.values[0], 
                df_hospede.telefone.values[0]
            )

            print("Hóspede Removido com Sucesso!")
            print(hospede_excluido.to_string())
        else:
            print(f"O Documento/CPF {documento} não existe.")

    def verifica_existencia_hospede(self, oracle:OracleQueries, documento:str=None) -> bool:
        df_hospede = oracle.sqlToDataFrame(f"select id_hospede from hospede where documento = '{documento}'")
        return df_hospede.empty
