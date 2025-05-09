import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from etl.abstract_etl import AbstractETL
from modelos.Genitor import Genitor
from modelos.Bebe import Bebe
from modelos.Cargo import Cargo
from modelos.ProfissionalSaude import ProfissionalSaude
from modelos.ProfissionalSaudeHasBebe import ProfissionalSaudeHasBebe


class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)

    def extract(self):
        self._dados_extraidos = {}
        nome_planilhas = pd.ExcelFile(self.origem).sheet_names
        for planilha in nome_planilhas:
            self._dados_extraidos[planilha] = pd.read_excel(self.origem, sheet_name=planilha)

    def transform(self):
        self._dados_transformados = {}
        if "Genitor" in self._dados_extraidos:
            self._dados_transformados["Genitor"] = Genitor.from_dataframe(self._dados_extraidos["Genitor"])
        if "Bebe" in self._dados_extraidos:
            self._dados_transformados["Bebe"] = Bebe.from_dataframe(self._dados_extraidos["Bebe"])
        if "Cargo" in self._dados_extraidos:
            self._dados_transformados["Cargo"] = Cargo.from_dataframe(self._dados_extraidos["Cargo"])
        if "Profissional_saude" in self._dados_extraidos:
            self._dados_transformados["Profissional_saude"] = ProfissionalSaude.from_dataframe(self._dados_extraidos["Profissional_saude"])
        if "Profissional_saude_has_Bebe" in self._dados_extraidos:
            self._dados_transformados["Profissional_saude_has_Bebe"] = ProfissionalSaudeHasBebe.from_dataframe(self._dados_extraidos["Profissional_saude_has_Bebe"])

    def load(self):
        engine = create_engine(self.destino)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        dados_genitor = self._dados_transformados["Genitor"]
        session.add_all(dados_genitor)
        dados_bebe = self._dados_transformados["Bebe"]
        session.add_all(dados_bebe)
        dados_cargo = self._dados_transformados["Cargo"]
        session.add_all(dados_cargo)
        dados_prof_saude = self._dados_transformados["Profissional_saude"]
        session.add_all(dados_prof_saude)
        dados_prof_has_bebe = self._dados_transformados["Profissional_saude_has_Bebe"]
        session.add_all(dados_prof_has_bebe)
        session.commit()
