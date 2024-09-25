from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuariosCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None

class UsuariosRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None

    class Config:
        from_attributes = True  # Atualizado para a nova configuração

class UsuariosUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    telefone: Optional[str] = None

class UsuariosReadMany(BaseModel):
    usuarios: list[UsuariosRead]
