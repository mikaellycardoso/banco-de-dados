from conexion.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.qry_total_hospedes = "SELECT COUNT(1) AS total_hospedes FROM hospede"
        self.qry_total_quartos = "SELECT COUNT(1) AS total_quartos FROM quarto"
        self.qry_total_reservas = "SELECT COUNT(1) AS total_reservas FROM reserva"

        self.created_by = """
        #        ANNA LUIZA
        #        MIKAELY
        #        AMON        
        #        LAISA   
        #        VICTORIA
        """

    def get_total_hospedes(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_hospedes)["total_hospedes"].values[0]

    def get_total_quartos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_quartos)["total_quartos"].values[0]

    def get_total_reservas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_reservas)["total_reservas"].values[0]

    

    def get_updated_screen(self):
        return f"""
        ########################################################
        #        SISTEMA DE CONTROLE DE RESERVAS E HÓSPEDES        
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - HÓSPEDES:        {str(self.get_total_hospedes()).rjust(5)}
        #      2 - QUARTOS:         {str(self.get_total_quartos()).rjust(5)}
        #      3 - RESERVAS:        {str(self.get_total_reservas()).rjust(5)}
        #     
        #
        #  CRIADO POR: {self.created_by}
        #
        #  RELATÓRIOS DISPONÍVEIS:
        #      - Ocupação dos quartos
        #      - Número de reservas por mês
        ########################################################
        """
