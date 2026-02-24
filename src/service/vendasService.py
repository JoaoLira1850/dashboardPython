from ..repository.vendasRepository import VendasRepository
import pandas as pd

class VendasService:

    def __init__(self):

        self.repository = VendasRepository()
        pass


    def listarVendasParaTabela(self):
        df = self.repository.findAll()

        return df
    
    def listarVendasPais(self) -> pd.DataFrame:
        df = self.repository.findAll()

        df = df.drop(columns=["datavenda","carro"], axis=1)

        df = df.groupby("pais")["preco"].sum().reset_index()


        return df
    
    def listarModelos(self):
        df = self.repository.findAll()
        df = df.drop(columns="datavenda", axis=1)
        df = df.groupby(["pais","carro"])["preco"].sum().reset_index()
        return df


