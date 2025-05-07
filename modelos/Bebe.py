from sqlalchemy import Column, String, Float, DateTime, ForeignKey, CheckConstraint, CHAR
from sqlalchemy.orm import relationship
from modelos.base import Base

class Bebe(Base.Base, Base):
    __tablename__ = "Bebe"
    nome = Column(String(200), primary_key=True, nullable=False)
    Genitor_mae_RG = Column(CHAR(15), ForeignKey("Genitor.RG", ondelete="CASCADE"), nullable=False)
    Genitor_pai_RG = Column(CHAR(15), ForeignKey("Genitor.RG"), nullable=True)
    dthr_nasc = Column(DateTime, nullable=False)
    sexo = Column(CHAR(1), nullable=False)
    peso = Column(Float, CheckConstraint('peso >= 0'), nullable=False)
    altura = Column(Float, CheckConstraint('altura >= 0'), nullable=False)
    tipo_parto = Column(String(45), nullable=False)

    mae = relationship("Genitor", foreign_keys=[Genitor_mae_RG], back_populates="bebes_mae")
    pai = relationship("Genitor", foreign_keys=[Genitor_pai_RG], back_populates="bebes_pai")
    profissionais = relationship("ProfissionalSaudeHasBebe", back_populates="bebe")
