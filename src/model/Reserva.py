from datetime import date
import decimal
from .Hospede import Hospede
from .Quarto import Quarto

class Reserva:
    def __init__(self,
                 id_reserva:int=None,
                 id_hospede:Hospede=None,
                 id_quarto:Quarto=None,
                 data_checkIn:date=None,
                 data_checkOut:date=None,
                 data_reserva:date=None,
                 valor_total:decimal=None,
                 quant_hospedes: int=None,
                 status: str=None
                 ):
        self.set_id_reserva(id_reserva)
        self.set_id_hospede(id_hospede)
        self.set_id_quarto(id_quarto)
        self.set_data_checkIn(data_checkIn)
        self.set_data_checkOut(data_checkOut)
        self.set_data_reserva(data_reserva)
        self.set_valor_total(valor_total)
        self.set_quant_hospedes(quant_hospedes)
        self.set_status(status)
    
    def set_id_reserva(self, id_reserva:int):
        self.id_reserva = id_reserva
        
    def set_id_hospede(self, id_hospede:Hospede):
        self.id_hospede = id_hospede
        
    def set_id_quarto(self, id_quarto:Quarto ):
        self.id_quarto = id_quarto
        
    def set_data_checkIn(self, data_checkIn:date):
        self.data_checkIn = data_checkIn
        
    def set_data_checkOut(self, data_checkOut:date):
        self.data_checkOut = data_checkOut
        
    def set_data_reserva(self, data_reserva:date):
        self.data_reserva = data_reserva
        
    def set_valor_total(self, valor_total:decimal):
        self.valor_total = valor_total
        
    def set_quant_hospedes(self, quant_hospedes:int):
        self.quant_hospedes = quant_hospedes
        
    def set_status(self, status:str):
        self.status = status
        
           
    def get_id_reserva(self) -> int:
        return self.id_reserva
    
    def get_id_hospede(self) -> Hospede:
        return self.id_hospede
    
    def get_id_quarto(self) -> int:
        return self.id_quarto
    
    def get_data_checkIn(self) -> date:
        return self.data_checkIn
    
    def get_data_checkOut(self) -> date:
        return self.data_checkOut
    
    def get_data_reserva(self) -> date:
        return self.data_reserva
    
    def get_valor_total(self) -> decimal:
        return self.valor_total
    
    def get_quant_hospedes(self) ->int:
        return self.quant_hospedes
    
    def get_status(self) -> str:
        return self.status
    
    def to_string(self) ->str:
        return f"ID da Reserva: {self.get_id_reserva()} |ID Hospede: {self.get_id_hospede()} ID Quarto: {self.get_id_quarto()}| Data do Check-In: {self.get_data_checkIn()} | Data do Check-Out: {self.get_data_checkOut()} | Data da Criação da Reserva: {self.get_data_reserva()} | Valor Total: {self.get_valor_total()} | Quant. de Hospedes: {self.get_quant_hospedes()} | Status da Reserva: {self.get_status()} "
    
    