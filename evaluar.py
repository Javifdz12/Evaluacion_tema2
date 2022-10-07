def funcion1():
    try:
        numero=7/0
        print(numero)
    except Exception:
        print('no se puede dividir entre 0')

def funcion2():
    try:
        lista = [4, 7, 30, 23, 5]
        print(lista[10])
    except Exception:
        print('indice incorrecto')

def funcion3():
    try:
        paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
        paises["alemania"]
    except Exception:
        print('clave incorrecta')

def funcion4():
    try:
        resultado = "2" + 10
        print(resultado)
    except Exception:
        print('no se pude sumar un str y un int')


