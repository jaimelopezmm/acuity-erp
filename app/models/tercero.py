from sqlalchemy import  Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from app.core.database import base

class tercero(base):
    __tablename__ = "terceros"
    id = Column(String,primary_key=True, index=True)#NIT o Cédula
    nombre = Column(String,nullable=False,index=True)
    direccion = Column(String,nullable=True)
    direccion = Column(String,nullable=True)
    telefono = Column(String,nullable=True)
    email = Column(String,nullable=True)
    empresa = Column(Integer,ForeignKey("empresas.id"),nullable=False)#Multi-tenant
    creado_en = Column(DateTime(timezone=True),server_default=func.now())
