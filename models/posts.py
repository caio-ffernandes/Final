from peewee import AutoField, CharField, TextField, ForeignKeyField, Model
from config.database import database
from models.subcategorias import SubcategoriasDB

class PostsDB(Model):
    id_post = AutoField()
    nome_post = CharField()
    descricao_post = TextField()
    imagem_post = CharField(null=True)  # Permitir valores nulos
    subcategorias_id_subcategoria = ForeignKeyField(
        SubcategoriasDB, backref='posts', column_name='subcategorias_id_subcategoria'
    )

    class Meta:
        database = database
        table_name = 'posts'
