class Hospede:
    def __init__(self, 
                 id_hospede:int=None,
                 documento:str=None, 
                 nome:str=None,
                 sobrenome:str=None,
                 email:str=None,
                 telefone:str=None
                ):
        
        self.set_id_hospede(id_hospede)
        self.set_documento(documento)
        self.set_nome(nome)
        self.set_sobrenome(sobrenome)
        self.set_email(email)
        self.set_telefone(telefone)
        
        
    def set_id_hospede(self, id_hospede:int):
        self.id_hospede = id_hospede
        
    def set_documento(self, documento:str):
        self.documento = documento

    def set_nome(self, nome:str):
        self.nome = nome
        
    def set_sobrenome(self, sobrenome:str):
        self.sobrenome = sobrenome

    def set_email(self, email:str):
        self.email = email
    
    def set_telefone(self, telefone:str):
        self.telefone = telefone
        
    def get_id_hospede(self) -> int:
        return self.id_hospede
    
    def get_documento(self) -> str:
        return self.documento

    def get_nome(self) -> str:
        return self.nome
    
    def get_sobrenome(self) -> str:
        return self.sobrenome

    def get_email(self) -> str:
        return self.email
    
    def get_telefone(self) ->str:
        return self.telefone
    
    
    def to_string(self) -> str:
        return f"ID Hospede: {self.get_id_hospede()} |  Documento: {self.get_documento()} | Nome Completo: {self.get_nome() + " " + self.get_sobrenome()} | Email: {self.get_email()} | Telefone: {self.get_telefone()}"
