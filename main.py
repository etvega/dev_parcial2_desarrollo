from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from connection import get_db, engine
from connection import Base
from models import schemas
from models.models import Usuario
from operation import main as operations

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def crear_usuario_endpoint(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = operations.crear_usuario(db, usuario)
    return schemas.UsuarioOut.from_orm_custom(nuevo_usuario)

@app.get("/usuarios/", response_model=list[schemas.UsuarioOut])
def obtener_usuarios_endpoint(db: Session = Depends(get_db)):
    usuarios = operations.obtener_usuarios(db)
    return [schemas.UsuarioOut.from_orm_custom(u) for u in usuarios]

@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def obtener_usuario_por_id_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    usuario = operations.obtener_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return schemas.UsuarioOut.from_orm_custom(usuario)

@app.patch("/usuarios/{usuario_id}/estado", response_model=schemas.UsuarioOut)
def actualizar_estado_usuario_endpoint(usuario_id: int, nuevo_estado: str, db: Session = Depends(get_db)):
    usuario = operations.actualizar_estado_usuario(db, usuario_id, nuevo_estado)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return schemas.UsuarioOut.from_orm_custom(usuario)

@app.patch("/usuarios/{usuario_id}/premium", response_model=schemas.UsuarioOut)
def hacer_usuario_premium_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    usuario = operations.hacer_usuario_premium(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return schemas.UsuarioOut.from_orm_custom(usuario)

@app.get("/usuarios/estado/{estado}", response_model=list[schemas.UsuarioOut])
def obtener_usuarios_por_estado_endpoint(estado: str, db: Session = Depends(get_db)):
    usuarios = operations.obtener_usuarios_por_estado(db, estado)
    return [schemas.UsuarioOut.from_orm_custom(u) for u in usuarios]

@app.get("/usuarios/premium-inactivos/", response_model=list[schemas.UsuarioOut])
def obtener_usuarios_premium_inactivos_endpoint(db: Session = Depends(get_db)):
    usuarios = operations.obtener_usuarios_premium_inactivos(db)
    return [schemas.UsuarioOut.from_orm_custom(u) for u in usuarios]

import webbrowser

@app.on_event("startup")
def mostrar_mensaje_inicio():
    print("\n✅ Servidor iniciado en: http://127.0.0.1:8000")
    print("🌐 Documentación Swagger disponible en: http://127.0.0.1:8000/docs\n")

# Abrir en el navegador de forma automatica
    webbrowser.open("http://127.0.0.1:8000/docs")
