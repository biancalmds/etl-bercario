from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, CHAR
from sqlalchemy.orm import relationship
from modelos.base import Base

class ProfissionalSaude(Base.Base, Base):
    __tablename__ = "Profissional_saude"
    CPF = Column(CHAR(11), primary_key=True, nullable=False)
    RG = Column(CHAR(15))
    nome = Column(String(200))
    dt_nasc = Column(DateTime)
    registro = Column(CHAR(45))
    Cargo_idCargo = Column(Integer, ForeignKey("Cargo.idCargo", ondelete="CASCADE"))

    cargo = relationship("Cargo", back_populates="profissionais")
    atendimentos = relationship("ProfissionalSaudeHasBebe", back_populates="profissional")