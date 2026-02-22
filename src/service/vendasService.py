from ..repository.vendasRepository import VendasRepository

class VendasService:

    def __init__(self):

        self.repository = VendasRepository()
        pass


    def listarVendasParaTabela(self):
        df = self.repository.findAll()

        return df
    
    def listarVendasPais(self):
        df = self.repository.findPaises()

        return df
    
    def listarModelos(self):
        df = self.repository.findModelos()

        return df


