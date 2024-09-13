from peewee import MySQLDatabase


database = MySQLDatabase(
    'brasil',
    user='root',
    #password='root',
    host='127.0.0.1',
    port=3306
)
def startup_db():
    if database.is_closed():
        database.connect()

    from models.culturas import CulturaDB
    from models.posts import PostsDB
    from models.subcategorias import SubcategoriasDB
    from models.tipo_responsavel import Tipo_RespDB

    database.create_tables(
        [
            CulturaDB,
            PostsDB,
            SubcategoriasDB,
            Tipo_RespDB
        ]
    )

def shutdown_db():
    database.close()