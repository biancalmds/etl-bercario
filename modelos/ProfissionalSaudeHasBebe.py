from sqlalchemy import Column, String, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from modelos.base import Base


class ProfissionalSaudeHasBebe(Base.Base, Base):
    __tablename__ = "Profissional_saude_has_Bebe"
    Profissional_saude_CPF = Column(CHAR(11), ForeignKey("Profissional_saude.CPF"), primary_key=True)
    Bebe_nome = Column(String(200), ForeignKey("Bebe.nome"), primary_key=True)
    Bebe_Genitor_mae_RG = Column(CHAR(15), ForeignKey("Genitor.RG"), primary_key=True)

    profissional = relationship("ProfissionalSaude", back_populates="atendimentos")
    bebe = relationship("Bebe", back_populates="profissionais")