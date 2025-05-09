# %%
# imports
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "./dads_bercario.xlsx"
destino = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(destino)
Session = sessionmaker(bind=engine)
session = Session()

etl = ETL(origem, destino)

#%%
## extraindo os dados
try:
    etl.extract()
except FileNotFoundError:
    print("Não foi possível encontrar o arquivo e extrair os dados dele.")

#%%
# transformando os dados
try:
    etl.transform()
except:
    pass

# %%
# carregando os dados no banco de dados
try:
    etl.load()
except IntegrityError:
    print("Esses registros já existem no banco de dados e não é possível inserir chaves duplicadas.")
    session.rollback()
