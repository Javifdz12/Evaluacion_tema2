from clases.alumno import alumno
from clases.producto import producto
def lanzar():
    alumno1=alumno('javi',6)
    print(alumno1.calificacion())
    print(alumno1.__str__())
    producto1=producto('1234','manzana',0.2,'Fruta')
    print(producto1.__str__())
    producto1.modificar_precio(0.3)
    print(producto1.__str__())
