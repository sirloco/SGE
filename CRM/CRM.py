import Oportunidad
class Cliente():

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Getters y Setters
    def getNombre(self):
        return self.nombre

    ###
    def setNombre(self, nombre):
        self.nombre = nombre


clientes = []

print("Escribe el nombre de cliente: ")

nombre = input()

c = Cliente(nombre)

clientes.append(c)

print(clientes[0].nombre)

clientes = Oportunidad.datos()

Oportunidad.


