from vehiculo import Vehiculo
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada


    def __str__(self):

        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    def catalogar1(self):
        return f'Soy un coche con estos atributos: {self.__str__()}'

    def catalogar2(self,y):
        if self.ruedas==y:
            return f'Soy un coche con estos atributos: {self.__str__()}'

