from clases.alumno import alumno
from clases.producto import producto
from coche import Coche
from vehiculo import Vehiculo
def catalogar2(list,y):
    for i in list:
        if i.ruedas==y:
            print(i.catalogar1())
        else:
            list.remove(i)
    print(f'Hay {len(list)} coches con {y} ruedas')

def lanzar():
    alumno1=alumno('javi',6)
    print(alumno1.calificacion())
    print(alumno1.__str__())
    producto1=producto('1234','manzana',0.2,'Fruta')
    print(producto1.__str__())
    producto1.modificar_precio(0.3)
    print(producto1.__str__())
    c1 = Coche("azul", 4, 150, 1200)
    c2 = Coche("rojo", 3, 140, 1000)
    print(c1)
    print(c1.catalogar1())
    list1=[c1,c2]
    for i in list1:
        print(i.catalogar1())
    print(catalogar2(list1,4))


