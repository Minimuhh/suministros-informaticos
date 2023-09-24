from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date, 
    ForeignKey
)
import connection

class Producto(connection.Base): 
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(length=40), nullable=False)
    description = Column(String(length=400), nullable=False)
    precio = Column(Integer, nullable=False)
    referencia = Column(String(length=50), nullable=True)
    color = Column(String(length=50), nullable=False)
    fecha_ingreso = Column(Date, default=False)
    fecha_entrega = Column(Date, default=False)

    def __init__(self, 
                 nombre, 
                 description, 
                 precio,
                 referencia, 
                 color, 
                 fecha_ingreso,
                 fecha_entrega
                 ): 

        self.nombre = nombre
        self.description = description
        self.precio = precio
        self.referencia = referencia
        self.color = color
        self.fecha_entrega = fecha_entrega
        self.fecha_ingreso = fecha_ingreso

    def __repr__(self):
        return f"Producto {self.id}: {self.nombre}"
    
    def __str__(self):
        return f"Producto {self.id}: {self.nombre}"


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


class Proveedor(connection.Base): 
    __tablename__ = "proveedor"

    id = Column(Integer, primary_key=True)
    comp_name = Column(String(length=40), nullable=False)
    email = Column(String(length=40), nullable=False)
    telefono = Column(String(length=10), nullable=False)
    direccion = Column(String(length=200), nullable=True)
    
    def __init__(self, 
                 comp_name, 
                 email,
                 telefono, 
                 direccion): 

        self.comp_name = comp_name
        self.email = email
        self.telefono = telefono 
        self.direccion = direccion

    
    def __repr__(self):
        return f"Empresa {self.id}: {self.comp_name} "
    
    def __str__(self):
        return f"Empresa {self.id}: {self.comp_name} "


class Pedido(connection.Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    product = Column(ForeignKey("producto.id"))
    user = Column(ForeignKey("usuario.id"))
    peso = Column(String(length=6), nullable=False)
    quantity = Column(String(length=4), nullable=False)
    fecha_pedido = Column(String(length= 60), nullable=False)
    fecha_entrega = Column(String(length= 60), nullable=False)

    def __init__(self,
                product,
                user,
                peso,
                quantity,
                fecha_pedido,
                fecha_entrega):

        self.product = product
        self.user = user
        self.peso = peso
        self.quantity = quantity
        self.fecha_pedido = fecha_pedido
        self.fecha_entrega = fecha_entrega
    

    def __repr__(self):
        return f"Pedido {self.id}: {self.product}, llegará el {self.fecha_entrega} "
    
    def __str__(self):
        return f"Pedido {self.id}: {self.product}, llegará el {self.fecha_entrega} "
