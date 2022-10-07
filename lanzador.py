from clases.alumno import alumno
def lanzar():
    alumno1=alumno('javi',6)
    print(alumno1.calificacion())
    print(alumno1.__str__())
