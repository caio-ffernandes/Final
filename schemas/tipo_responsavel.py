from pydantic import BaseModel

class ResponsavelCreate(BaseModel):
    nome_responsavel: str

class ResponsavelRead(BaseModel):
    id_responsavel: int
    nome_responsavel: str

class ResponsavelUpdate(BaseModel):
    nome_responsavel: str

class ResponsavelReadMany(BaseModel):
    responsavels: list[ResponsavelCreate]
