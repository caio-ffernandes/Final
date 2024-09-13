from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.culturas import CulturaDB

class SubcategoriasDB(Model):
    id_subcategoria = AutoField()
    nome_subcategoria = CharField()
    culturas = ForeignKeyField(
        model=CulturaDB, backref='subcategorias'
    )

    class Meta:
        database = database
        table_name = 'subcategorias'
