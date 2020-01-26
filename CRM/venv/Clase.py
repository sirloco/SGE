class Oportunidad:

    __activiNuevas = []
    __activiCalificadas = []
    __activiPropuestas = []
    __activiGanadas = []

    # Constructor
    def __init__(self, nombre):
        self.__nombre = nombre

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getNuevas(self):
        return self.__activiNuevas

    def getCalificadas(self):
        return self.__activiCalificadas

    def getPropuestas(self):
        return self.__activiPropuestas

    def getGanadas(self):
        return self.__activiGanadas

class Cliente:

    __oportunidades = Oportunidad

    # Constructor
    def __init__(self, nombre, empresa):
        self.__nombre = nombre
        self.__empresa = empresa

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getEmpresa(self):
        return self.__empresa

    #este lo dejo para ver como se escribe el set
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getOportunidad(self):
        return self.__oportunidades

class Actividad:

    __oportunidad = Oportunidad

    # Constructor
    def __init__(self, nombre, descripcion, fecha):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha = fecha

    # Getters y Setters
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def getFecha(self):
        return self.__fecha
    def setOportunidad(self, oportunidad):
        self.__oportunidad = oportunidad

