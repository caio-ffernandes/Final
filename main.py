from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from config.database import shutdown_db, startup_db
from routers.culturas import router as culturas_router
from routers.posts import router as posts_router
from routers.subcategorias import router as subcategorias_router
from routers.tipo_responsavel import router as tipo_responsavel_router
from routers.responsaveis import router as responsaveis_router
from routers.usuarios import router as usuarios_router
from routers.usuariospost import router as usuarios_posts_router
app = FastAPI(title='SITE CULTURAL BRASILEIRO')
app.mount("/static", StaticFiles(directory="static/uploads"), name="static")
app.add_event_handler("startup", startup_db)
app.add_event_handler("shutdown", shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def status():
    return {"message": "Hello World"}

@app.get("/images/{image_name}")
async def serve_image(image_name: str):
    image_path = f"static/uploads/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}
@app.get("/posts/{image_name}")
async def post_image(image_name: str):
    image_path = f"static/uploads/posts/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}
@app.get("/responsaveis/{image_name}")
async def responsaveis_image(image_name: str):
    image_path = f"static/uploads/responsaveis/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}

app.include_router(culturas_router)
app.include_router(posts_router)
app.include_router(subcategorias_router)
app.include_router(tipo_responsavel_router)
app.include_router(responsaveis_router)
app.include_router(usuarios_router)
app.include_router(usuarios_posts_router)