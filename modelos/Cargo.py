from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from modelos.base import Base

class Cargo(Base.Base, Base):
    __tablename__ = "Cargo"
    idCargo = Column(Integer, primary_key=True, nullable=False)
    nome_cargo = Column(String(200))
    descricao = Column(String(1000))

    profissionais = relationship("ProfissionalSaude", back_populates="cargo")