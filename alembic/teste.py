# import os
# from sqlalchemy import create_engine, inspect

# usuario = os.getenv("USUARIO")
# senha = os.getenv("SENHA")
# host = os.getenv("HOST")
# banco_de_dados = os.getenv("BANCO_DE_DADOS")
# engine = create_engine(f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server")

# insp = inspect(engine)
# print(insp.get_table_names())