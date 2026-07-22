from sqlalchemy import Column, String, Integer, Numeric, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import   base

class comprobantEgreso(base):
    __tablename__ = "Comprobantes_de_egreso"

    id = Column(Integer,primary_key=True, autoincrement=True)
    numero = Column(String, nullable=False, index=True)
    fecha = Column(Date,nullable=False)
    subtotal = Column(Numeric(precision=14, scale=2),default=0.0)
    retefuente = Column(Numeric(precision=14, scale=2),default=0.0)
    total = Column(Numeric(precision=14, scale=2),default=0.0)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    creado_en =Column(DateTime(timezone=True),server_default=func.now())