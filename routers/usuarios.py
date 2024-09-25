from fastapi import APIRouter, HTTPException
from models.usuarios import UsuariosDB
from schemas.usuarios import (
    UsuariosCreate,
    UsuariosRead,
    UsuariosReadMany,
    UsuariosUpdate
)

router = APIRouter(prefix='/usuarios', tags=['USUARIOS'])

@router.post('', response_model=UsuariosRead)
def criar_usuario(novo_usuario: UsuariosCreate):
    usuario = UsuariosDB.create(**novo_usuario.dict())
    return UsuariosRead.from_orm(usuario)

@router.get('', response_model=UsuariosReadMany)
def listar_usuarios():
    usuarios = UsuariosDB.select()
    usuarios_list = [UsuariosRead.from_orm(usuario) for usuario in usuarios]
    return {'usuarios': usuarios_list}

@router.get('/{usuario_id}', response_model=UsuariosRead)
def listar_usuario(usuario_id: int):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UsuariosRead.from_orm(usuario)

@router.patch('/{usuario_id}', response_model=UsuariosRead)
def atualizar_usuario(usuario_id: int, usuario_atualizado: UsuariosUpdate):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario_data = usuario_atualizado.dict(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(usuario, key, value)

    usuario.save()
    return UsuariosRead.from_orm(usuario)

@router.delete('/{usuario_id}', response_model=dict)
def excluir_usuario(usuario_id: int):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.delete_instance()
    return {'message': 'Usuário excluído com sucesso'}
