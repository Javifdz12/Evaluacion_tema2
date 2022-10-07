class producto:
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
    def __str__(self):
        return f'Producto:\n-Nombre:{self.nombre}\n-Codigo:{self.codigo}\n-Tipo:{self.tipo}\n-Precio:{self.precio}'
    def modificar_precio(self,x):
        self.precio=x
