from peewee import MySQLDatabase

# Conexão com o banco de dados MySQL
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

    # Importação dos modelos
    from models.culturas import CulturaDB
    from models.posts import PostsDB
    from models.subcategorias import SubcategoriasDB
    from models.tipo_responsavel import Tipo_RespDB
    from models.responsaveis import ResponsaveisDB
    from models.usuarios import UsuariosDB
    from models.usuariospost import UsuariosHasPostsDB

    # Criação das tabelas
    database.create_tables(
        [
            CulturaDB,
            PostsDB,
            SubcategoriasDB,
            Tipo_RespDB,
            ResponsaveisDB,
            UsuariosDB,
            UsuariosHasPostsDB
        ]
    )

def shutdown_db():
    if not database.is_closed():
        database.close()
