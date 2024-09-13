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
    # Verifica se a subcategoria existe
    subcategoria = SubcategoriasDB.get_or_none(
        SubcategoriasDB.id_subcategoria == novo_post.subcategorias_id_subcategoria)
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")

    # Cria o novo post
    post = PostsDB.create(
        nome_post=novo_post.nome_post,
        descricao_post=novo_post.descricao_post,
        imagem_post=novo_post.imagem_post,
        subcategorias_id_subcategoria=novo_post.subcategorias_id_subcategoria
    )
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

    post.nome_post = post_atualizado.nome_post or post.nome_post
    post.descricao_post = post_atualizado.descricao_post or post.descricao_post
    post.imagem_post = post_atualizado.imagem_post or post.imagem_post
    post.subcategorias_id_subcategoria = post_atualizado.subcategorias_id_subcategoria or post.subcategorias_id_subcategoria
    post.save()
    return post


@router.delete('/{post_id}', response_model=dict)
def excluir_post(post_id: int):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    post.delete_instance()
    return {'message': 'Post excluído com sucesso'}
