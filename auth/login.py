from fastapi import APIRouter, Depends, HTTPException
from models.usuarios import UsuariosDB
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Configurações JWT
SECRET_KEY = "seu_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()


# Função de autenticação
def autenticar_usuario(email: str, senha: str):
    usuario = UsuariosDB.get_or_none(UsuariosDB.email == email)
    if usuario and usuario.senha == senha:  # Substitua por um hash de senha adequado
        return usuario
    return None


# Função de login para gerar token
@router.post("/login")
def login_usuario(email: str, senha: str):
    usuario = autenticar_usuario(email, senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    # Geração do token JWT
    token_data = {
        "sub": usuario.email,
        "tipo": usuario.tipo  # Verifica se o usuário é 'admin' ou 'comum'
    }
    token_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token_jwt, "token_type": "bearer"}


# Função para verificar o token
def verificar_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


# Exemplo de rota protegida para admins
@router.get("/admin")
def rota_protegida(token: str = Depends(verificar_token)):
    if token.get("tipo") != "admin":
        raise HTTPException(status_code=403, detail="Acesso negado")
    return {"message": "Bem-vindo ao painel administrativo"}
