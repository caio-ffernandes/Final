from fastapi import APIRouter, HTTPException
from models.tipo_responsavel import Tipo_RespDB
from schemas.tipo_responsavel import (
    ResponsavelCreate,
    ResponsavelRead,
    ResponsavelReadMany,
    ResponsavelUpdate
)

router = APIRouter(prefix='/responsaveis', tags=['RESPONSAVEIS'])

@router.post('', response_model=ResponsavelRead)
def criar_responsavel(novo_responsavel: ResponsavelCreate):
    responsavel = Tipo_RespDB.create(**novo_responsavel.dict())
    return responsavel

@router.get('', response_model=ResponsavelReadMany)
def listar_responsaveis():
    responsaveis = Tipo_RespDB.select()
    return {'responsaveis': responsaveis}

@router.get('/{responsavel_id}', response_model=ResponsavelRead)
def listar_responsavel(responsavel_id: int):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")
    return responsavel

@router.patch('/{responsavel_id}', response_model=ResponsavelRead)
def atualizar_responsavel(responsavel_id: int, responsavel_atualizado: ResponsavelUpdate):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    responsavel.nome = responsavel_atualizado.nome or responsavel.nome
    responsavel.save()
    return responsavel

@router.delete('/{responsavel_id}', response_model=dict)
def excluir_responsavel(responsavel_id: int):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    responsavel.delete_instance()
    return {'message': 'Responsável excluído com sucesso'}
