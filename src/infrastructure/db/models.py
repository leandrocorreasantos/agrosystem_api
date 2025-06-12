from src.infrastructure.db import db
from src.infrastructure.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class ProdutorModel(Base):
    __tablename__ = 'produtores_rurais'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(), unique=True, nullable=False)
    propriedades = db.relationship('PropriedadeModel', backref='produtor', cascade="all, delete-orphan")


class PropriedadeModel(Base):
    __tablename__ = 'propriedades_rurais'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String, nullable=False)
    area_total = db.Column(db.Float, nullable=False)
    area_agricultavel = db.Column(db.Float, nullable=False)
    area_vegetacao = db.Column(db.Float, nullable=False)
    produtor_id = db.Column(UUID(as_uuid=True), db.ForeignKey('produtores_rurais'), nullable=False)
    safras = db.relationship("SafraModel", backref="propriedade", cascade="all, delete-orphan")


class SafraModel(Base):
    __tablename__ = 'safras'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ano = db.Column(db.String(10), nullable=False)
    propriedade_id = db.Column(UUID(as_uuid=True), db.ForeignKey("propriedades_rurais"), nullable=False)
    culturas = db.relationship("CulturaModel", backref="safra", cascade="all, delete-orphan")


class CulturaModel(Base):
    __tablename__ = "culturas"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String, nullable=False)
    area_utilizada = db.Column(db.Float, nullable=False)
    safra_id = db.Column(UUID(as_uuid=True), db.ForeignKey("safras.id"), nullable=False)
    safra = db.relationship("SafraModel", backref="culturas", cascade="all, delete-orphan")

