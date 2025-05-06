import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from etl.abstract_etl import AbstractETL
from modelos.user import User


class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)

    def extract(self):
        pass

    def transform(self):
        pass

    def load(self):
        pass
