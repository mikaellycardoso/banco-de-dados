from datetime import date
import decimal
from .Reserva import Reserva

class Pagamento:
    def __init__(self,
                 id_pagamento:int=None,
                 id_reseva:Reserva=None,
                 valor_pago:decimal=None,
                 data_pagamento:date=None,
                 metodo:str=None,
                 status:str=None
                ):
        
        self.set_id_pagamento(id_pagamento)
        self.set_id_reserva(id_reseva)
        self.set_valor_pago(valor_pago)
        self.set_data_pagamento(data_pagamento)
        self.set_metodo(metodo)
        self.set_status(status)
    
    def set_id_pagamento(self, id_pagamento:int):
        self.id_pagamento = id_pagamento
        
    def set_id_reserva(self, id_reserva:Reserva):
        self.id_reserva = id_reserva
        
    def set_valor_pago(self, valor_pago:decimal):
        self.valor_pago = valor_pago
        
    def set_data_pagamento(self, data_pagamento:date):
        self.data_pagamento = data_pagamento
        
    def set_metodo(self, metodo:str):
        self.metodo = metodo
        
    def set_status(self, status:str):
        self.status = status

    
    def get_id_pagamento(self) -> int:
        return self.id_pagamento
    
    def get_id_reserva(self) -> Reserva:
        return self.id_reserva
    
    def get_valor_pago(self) -> decimal:
        return self.valor_pago
    
    def get_data_pagamento(self) -> date:
        return self.data_pagamento
    
    def get_metodo(self) -> str:
        return self.metodo
    
    def get_status(self) -> str:
        return self.status
    
    def to_string(self) ->str:
        return f"ID Pagamento: {self.get_id_pagamento()} | ID Reserva: {self.get_id_reserva()} | Valor Pago: {self.get_valor_pago()} | Data do Pagamento: {self.get_data_pagamento()} | Método de Pagamento: {self.get_metodo()} | Status do Pagamento: {self.get_status()}"