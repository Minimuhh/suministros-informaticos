from sqlalchemy import Column, Integer, String, Boolean
import connection



# class Producto(connection.Base): 
#     __tablename__ = "producto"


class Usuario(connection.Base): 
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(length=40), nullable=False)
    apellido = Column(String(length=50), nullable=False)
    email = Column(String(length=40), nullable=False)
    telefono = Column(String(length=10), nullable=False)
    direccion = Column(String(length=200), nullable=True)
    password = Column(String(length=50), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __init__(self, 
                 nombre, 
                 apellido, 
                 email,
                 telefono, 
                 direccion, 
                 password, 
                 is_admin): 

        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono 
        self.direccion = direccion
        self.password = password
        self.is_admin = is_admin
    
    def __repr__(self):
        return f"Usuario {self.id}: {self.nombre} {self.apellido}"
    
    def __str__(self):
        return f"Usuario {self.id}: {self.nombre} {self.apellido}"


# class Proveedor(connection.Base): 
#     pass