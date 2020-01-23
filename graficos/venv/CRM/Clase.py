class Cliente():

    __oportunidades = ["oportunidad1","oportunidad2"]

    # guarda el nombre del cliente y la empresa a la que pertenece
    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa

    # getter method
    def Oportunidad(self):
        return self.__oportunidades




