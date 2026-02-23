from urllib.parse import quote_plus

class Settings:
    DB_USER = "neondb_owner"
    DB_PASS = "npg_67ZPnuLdrxiB"
    DB_HOST = "ep-divine-hall-ace1mdl4-pooler.sa-east-1.aws.neon.tech"
    DB_PORT = "5432"
    DB_NAME = "neondb"

    @property
    def database_url(self):
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{quote_plus(self.DB_PASS)}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            f"?sslmode=require"
        )

settings = Settings()