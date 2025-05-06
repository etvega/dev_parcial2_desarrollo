from sqlalchemy.orm import Session
from models.models import Usuario
from models.schemas import UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def actualizar_estado_usuario(db: Session, usuario_id: int, nuevo_estado: str):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        usuario.estado = nuevo_estado
        db.commit()
        db.refresh(usuario)
    return usuario

def hacer_usuario_premium(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        usuario.premium = True
        db.commit()
        db.refresh(usuario)
    return usuario

def obtener_usuarios_por_estado(db: Session, estado: str):
    return db.query(Usuario).filter(Usuario.estado == estado).all()

def obtener_usuarios_premium_inactivos(db: Session):
    return db.query(Usuario).filter(Usuario.estado == "Inactivo", Usuario.premium == True).all()