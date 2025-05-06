from sqlalchemy import Column, String, Float, Date, DateTime, ForeignKey, CheckConstraint, Integer, CHAR
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


class Cargo(Base.Base, Base):
    __tablename__ = "Cargo"
    idCargo = Column(Integer, primary_key=True, nullable=False)
    nome_cargo = Column(String(200))
    descricao = Column(String(1000))

    profissionais = relationship("ProfissionalSaude", back_populates="cargo")


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


class ProfissionalSaudeHasBebe(Base.Base, Base):
    __tablename__ = "Profissional_saude_has_Bebe"
    Profissional_saude_CPF = Column(CHAR(11), ForeignKey("Profissional_saude.CPF"), primary_key=True)
    Bebe_nome = Column(String(200), ForeignKey("Bebe.nome"), primary_key=True)
    Bebe_Genitor_mae_RG = Column(CHAR(15), ForeignKey("Genitor.RG"), primary_key=True)

    profissional = relationship("ProfissionalSaude", back_populates="atendimentos")
    bebe = relationship("Bebe", back_populates="profissionais")