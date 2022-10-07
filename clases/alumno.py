class alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota=nota
    def calificacion(self):
        if self.nota>=5:
            return f'Aprobado'
        else:
            return f'Suspenso'
    def __str__(self):
        return f'el alumno {self.nombre} ha sacado un {self.nota}'

