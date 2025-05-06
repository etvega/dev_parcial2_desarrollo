from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str
    estado: str
    premium: str  # Se mostrará como "Sí" o "No"

    class Config:
        orm_mode = True

    @staticmethod
    def from_orm_custom(usuario):
        return UsuarioOut(
            id=usuario.id,
            nombre=usuario.nombre,
            email=usuario.email,
            estado=usuario.estado,
            premium="Sí" if usuario.premium else "No"
        )