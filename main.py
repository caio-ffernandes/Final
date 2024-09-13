from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from config.database import shutdown_db, startup_db
from routers.culturas import router as culturas_router
from routers.posts import router as posts_router
from routers.subcategorias import router as subcategorias_router
from routers.tipo_responsavel import router as tipo_responsavel_router
app = FastAPI(title='SITE CULTURAL BRASILEIRO')

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

app.include_router(culturas_router)
app.include_router(posts_router)
app.include_router(subcategorias_router)
app.include_router(tipo_responsavel_router)