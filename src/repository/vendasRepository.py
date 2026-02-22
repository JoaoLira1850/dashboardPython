import pandas as pd
from ..database.connections import DatabaseConnection


class VendasRepository:
    def __init__(self):

        self.db = DatabaseConnection()
        self.engine = self.db.get_engine()
        pass

    def _load_query(self, query_name: str) -> str:

        file_path = f"src/query/{query_name}.sql"

        with open(file_path, 'r' , encoding='utf-8') as file:
            return file.read()


    def findAll(self):

        query: str = self._load_query("queryFindTableCarros")

        return pd.read_sql(query, self.engine)
    

    
    def findPaises(self):
        query: str = self._load_query("queryVendasCarrosPais")

        return pd.read_sql(query, self.engine)
    
    def findModelos(self):

        query: str = self._load_query("queryVendasModelos")

        return pd.read_sql(query,self.engine)