from conexion.oracle_queries import OracleQueries
import os 

class Relatorio:
    def __init__(self):
        # 1. Obtém o diretório atual do arquivo (src/reports/)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 2. CORREÇÃO: Define o caminho base subindo UM nível (reports/ -> src/)
        # e depois descendo para a pasta 'sql' (dentro de src/).
        sql_base_path = os.path.join(current_dir, "..", "sql") 
        
        # --- Carga dos Arquivos SQL ---

        # 1. Relatório de Hospedes
        with open(os.path.join(sql_base_path, "relatorio_hospede.sql"), "r") as f:
            self.query_relatorio_hospede = f.read()

        # 2. Relatório de Quartos
        with open(os.path.join(sql_base_path, "relatorio_quartos.sql"), "r") as f:
            self.query_relatorio_quartos = f.read()

        # 3. Relatório de Tipos de Quartos
        with open(os.path.join(sql_base_path, "relatorio_tipos_quartos.sql"), "r") as f:
            self.query_relatorio_tipos_quartos = f.read()

        # 4. Relatório de Reservas
        with open(os.path.join(sql_base_path, "relatorio_reservas.sql"), "r") as f:
            self.query_relatorio_reservas = f.read()

        # 5. Relatório de Pagamentos
        with open(os.path.join(sql_base_path, "relatorio_pagamentos.sql"), "r") as f:
            self.query_relatorio_pagamentos = f.read()
    def get_relatorio_hospede(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_hospede))
        input("Pressione Enter para Sair do Relatório de Hospede")

    def get_relatorio_quartos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_quartos))
        input("Pressione Enter para Sair do Relatório de Quartos")

    def get_relatorio_tipos_quartos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_tipos_quartos))
        input("Pressione Enter para Sair do Relatório de Tipos de Quarto")

    def get_relatorio_reservas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_reservas))
        input("Pressione Enter para Sair do Relatório de Reservas")

    def get_relatorio_pagamentos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pagamentos))
        input("Pressione Enter para Sair do Relatório de Pagamentos")
