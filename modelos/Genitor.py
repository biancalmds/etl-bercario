from sqlalchemy import Column, String, Date, CHAR
from sqlalchemy.orm import relationship
from modelos.base import Base


class Genitor(Base.Base, Base):
    __tablename__ = "Genitor"
    RG = Column(CHAR(15), primary_key=True, nullable=False)
    nome = Column(String(200), nullable=False)
    sexo = Column(CHAR(1), nullable=False)
    dt_nascimento = Column(Date, nullable=False)
    telefone = Column(CHAR(15), nullable=False)
    endereco = Column(String(500), nullable=False)

    bebes_mae = relationship("Bebe", back_populates="mae", foreign_keys="Bebe.Genitor_mae_RG")
    bebes_pai = relationship("Bebe", back_populates="pai", foreign_keys="Bebe.Genitor_pai_RG")