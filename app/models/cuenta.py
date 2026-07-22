from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class CuentaContable(Base):
    tablename = "cuentas_contables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable=False, index=True)  # Ej: '110505'
    nombre = Column(String(150), nullable=False)             # Ej: 'Caja General'
    nivel = Column(Integer, nullable=False)                  # Ej: 1 (Clase), 2 (Grupo), ..., 5 (Auxiliar)
    permite_movimiento = Column(Boolean, default=True)       # Solo se asienta en cuentas auxiliares
    
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)