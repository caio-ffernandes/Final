from pydantic import BaseModel

class SubcategoriasCreate(BaseModel):
    nome_subcategoria: str
    culturas_id_cultura: int

class SubcategoriasRead(BaseModel):
    id_subcategoria: int
    nome_subcategoria: str
    culturas_id_cultura: int

class SubcategoriasUpdate(BaseModel):
    nome_subcategoria: str
    culturas_id_cultura: int

class SubcategoriasReadMany(BaseModel):
    subcategorias: list[SubcategoriasRead]
