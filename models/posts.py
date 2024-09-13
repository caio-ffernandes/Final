from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.subcategorias import SubcategoriasDB

class PostsDB(Model):
    id_post = AutoField()
    nome_post = CharField()
    descricao_post = CharField()
    imagem_post = CharField()
    subcategorias_id_subcategoria = ForeignKeyField(
        model=SubcategoriasDB, backref='posts'
    )

    class Meta:
        database = database
        table_name = 'posts'
