from pydantic import BaseModel

class PostsCreate(BaseModel):
    nome_post: str
    descricao_post: str
    imagem_post: str
    subcategorias_id_subcategoria: int

class PostsRead(BaseModel):
    id_post: int
    nome_post: str
    descricao_post: str
    imagem_post: str
    subcategorias_id_subcategoria: int

class PostsUpdate(BaseModel):
    nome_post: str
    descricao_post: str
    imagem_post: str
    subcategorias_id_subcategoria: int

class PostsReadMany(BaseModel):
    posts: list[PostsRead]
