from .tipo_quarto import tipo_quarto

class Quarto:
    def __init__(self, 
                 id_quarto:int=None,
                 numero_quarto:int=None, 
                 andar_quarto:int=None,
                 tipo:tipo_quarto=None,
                 status:str=None
                 ):
        
        self.set_id_quarto(id_quarto)
        self.set_numero_quarto(numero_quarto)
        self.set_andar_quarto(andar_quarto)
        self.set_tipo(tipo)
        self.set_status(status)

    def set_id_quarto(self, id_quarto:int):
        self.id_quarto = id_quarto
    
    def set_numero_quarto(self, numero_quarto:int):
        self.numero_quarto = numero_quarto

    def set_andar_quarto(self, andar_quarto:int):
        self.andar_quarto = andar_quarto
        
    def set_tipo(self, tipo:tipo_quarto):
        self.tipo = tipo
        
    def set_status(self, status:str):
        self.status = status

    def get_id_quarto(self) -> int:
        return self.id_quarto
    
    def get_numero_quarto(self) -> int:
        return self.numero_quarto

    def get_andar_quarto(self) -> int:
        return self.andar_quarto

    def get_tipo(self) -> str:
        return self.tipo
    
    def get_status(self) -> str:
        return self.status

    def to_string(self) -> str:
        return f"ID Quarto: {self.get_id_quarto()} | Número do Quarto: {self.get_numero_quarto()} | Andar: {self.get_andar_quarto()} | Tipo: {self.get_tipo().get_nome_tipo()} | Status do Quarto: {self.get_status()} "