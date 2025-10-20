import decimal

class tipo_quarto:
    def __init__(self,
                 id_tipo_quarto:int=None,
                 nome_tipo:str=None,
                 descricao_tipo: str=None,
                 capacidade_maxima:int=None,
                 preco_diaria:decimal=None,
                 ):
        
        self.set_id_tipo_quarto(id_tipo_quarto)
        self.set_nome_tipo(nome_tipo)
        self.set_descricao_tipo(descricao_tipo)
        self.set_capacidade_maxima(capacidade_maxima)
        self.set_preco_diaria(preco_diaria)
    
    def set_id_tipo_quarto(self, id_tipo_quarto:int):
        self.id_tipo_quarto = id_tipo_quarto
        
    def set_nome_tipo(self, nome_tipo:str):
        self.nome_tipo = nome_tipo
        
    def set_descricao_tipo(self, descricao_tipo:str):
        self.descricao_tipo = descricao_tipo
        
    def set_capacidade_maxima(self, capacidade_maxima:int):
        self.capacidade_maxima = capacidade_maxima
        
    def set_preco_diaria(self, preco_diario:decimal):
        self.preco_diaria = preco_diario
    
    def get_id_tipo_quarto(self) -> int:
        return self.id_tipo_quarto
    
    def get_nome_tipo(self) -> str:
        return self.nome_tipo
    
    def get_descricao_tipo(self) -> str:
        return self.descricao_tipo
    
    def get_capacidade_maxima(self) -> int:
        return self.capacidade_maxima
    
    def get_preco_diaria(self) -> decimal:
        return self.preco_diaria
     
    def to_string(self) -> str:
        return f"ID tipo Quarto: {self.get_id_tipo_quarto()} | Tipo Quarto: {self.get_nome_tipo()} | Descrição: {self.get_descricao_tipo()} | Capacidade Max: {self.get_capacidade_maxima()} | Preço Diária: {self.get_preco_diaria()} "