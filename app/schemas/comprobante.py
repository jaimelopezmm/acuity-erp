from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional

#Esquema para creat un comprobante de egreso

class comprobanteEgresoCreate(BaseModel):
    numero : str
    id_beneficiario : str
    id_emisor : str
    fecha : date
    subtotal : Decimal
    retefuente : Decimal
    total : Decimal
#Esquema de respuesta para el usuario / frontend
class comprobanteEgresoResponse(comprobanteEgresoCreate):
    id:int


    class config:
        from_atributes = True