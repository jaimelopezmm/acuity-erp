from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session
from typing import List

from app.core.database import get_db
from app.models.tercero import tercero
from app.models.comprobante import comprobanteEgreso
from app.schemas.comprobante import comprobanteEgresoCreate, comprobanteEgresoResponse

router = APIRouter(prefix="/comprobantes-egreso", tags=["Comprobantes de Egreso"])

@router.post("/", response_model=comprobanteEgresoResponse, status_code=status.HTTP_201_CREATED)
def crear_comprobante_egreso(
    comprobante_in: comprobanteEgresoCreate, 
    empresa_id: int = 1, # Temporalmente fijo hasta agregar JWT
    db: session = Depends(get_db)
):
    # 1. Validar si el número de comprobante ya existe para esta empresa
    existente = db.query(comprobanteEgreso).filter(
        comprobanteEgreso.numero == comprobante_in.numero,
        comprobanteEgreso.empresa_id == empresa_id
    ).first()
    
    if existente:
        raise HTTPException(
            status_code=400, 
            detail="El número de Comprobante de Egreso ya se encuentra registrado."
        )

    # 2. Validar que beneficiario y emisor existan en la tabla terceros
    beneficiario = db.query(tercero).filter(tercero.id == comprobante_in.id_beneficiario).first()
    emisor = db.query(tercero).filter(tercero.id == comprobante_in.id_emisor).first()

    if not beneficiario or not emisor:
        raise HTTPException(
            status_code=400, 
            detail="El ID del beneficiario o del emisor no existe en la base de datos de terceros."
        )

    # 3. Guardar en la BD
    nuevo_comprobante = comprobanteEgreso(
        **comprobante_in.model_dump(),
        empresa_id=empresa_id
    )
    
    db.add(nuevo_comprobante)
    db.commit()
    db.refresh(nuevo_comprobante)
    
    return nuevo_comprobante