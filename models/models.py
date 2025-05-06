from sqlalchemy import Column, Integer, String, Boolean
from connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    estado = Column(String, default="Activo")  # "Activo" o "Inactivo"
    premium = Column(Boolean, default=False)   # True (Sí), False (No)