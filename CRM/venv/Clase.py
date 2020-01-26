# ///////////////////////// CLASE OPORTUNIDAD////////////////////
class Oportunidad:
    __actividades = []

    # Constructor
    def __init__(self, nombre):
        self.__nombre = nombre

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getActividades(self):
        return self.__actividades


#################################################################

# //////////////////// CLASE CLIENTE /////////////////////////////
class Cliente:
    __oportunidad = Oportunidad

    # Constructor
    def __init__(self, nombre, empresa):
        self.__nombre = nombre
        self.__empresa = empresa

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getEmpresa(self):
        return self.__empresa

    # este lo dejo para ver como se escribe el set
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getOportunidad(self):
        return self.__oportunidad

    def setOportunidad(self, Oportunidad):
        self.__oportunidad = Oportunidad


#################################################################

# ////////////////////// CLASE ACTIVIDAD ////////////////////////
class Actividad:
    etapas = {0: "Nueva", 1: "calificada", 2: "Propuesta", 3: "Ganada"}

    __oportunidad = Oportunidad

    # Constructor
    def __init__(self, nombre, descripcion, fecha):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha = fecha
        self.__etapa = self.etapas.get(0)

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def getFecha(self):
        return self.__fecha

    def setOportunidad(self, oportunidad):
        self.__oportunidad = oportunidad

    def setEtapa(self, etap):
        self.__etapa = self.etapas.get(etap)

    def getEtapa(self):
        return self.__etapa
