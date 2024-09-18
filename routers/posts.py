from fastapi import APIRouter, HTTPException
from models.posts import PostsDB, SubcategoriasDB
from schemas.posts import (
    PostsCreate,
    PostsRead,
    PostsReadMany,
    PostsUpdate
)

router = APIRouter(prefix='/posts', tags=['POSTS'])


@router.post('', response_model=PostsRead)
def criar_post(novo_post: PostsCreate):

    subcategoria = SubcategoriasDB.get_or_none(
        SubcategoriasDB.id_subcategoria == novo_post.subcategorias_id_subcategoria)
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")

    post = PostsDB.create(**novo_post.dict())
    return post


@router.get('', response_model=PostsReadMany)
def listar_posts():
    posts = PostsDB.select()
    return {'posts': posts}


@router.get('/{post_id}', response_model=PostsRead)
def listar_post(post_id: int):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return post


@router.patch('/{post_id}', response_model=PostsRead)
def atualizar_post(post_id: int, post_atualizado: PostsUpdate):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    # Atualiza apenas os campos fornecidos
    post_data = post_atualizado.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(post, key, value)

    post.save()
    return post


@router.delete('/{post_id}', response_model=dict)
def excluir_post(post_id: int):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    post.delete_instance()
    return {'message': 'Post excluído com sucesso'}
