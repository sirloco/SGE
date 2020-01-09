class Oportunidad():

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre

    actividades = []

    # Getters y Setters
    def getActividad(self):
        return self.actividades




class Actividad():

    # Constructor
    def __init__(self, nombre, fecha, descripcion):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion


def datos():
    clientes = ["pepe", "juan"]
    return clientes


def ganadas():
    ganadas = []
    ganadas.append(Actividad("coleccion datos", "01/02/20", "Escanear temperaturas"))
    ganadas.append(Actividad("entrevistas", "01/02/20", "entrevista con cliente"))
    return ganadas


def calificados():
    ganadas = []
    ganadas.append(Actividad("coleccion datos", "01/02/20", "Escanear temperaturas"))
    ganadas.append(Actividad("entrevistas", "01/02/20", "entrevista con cliente"))
    return ganadas


def propuestas():
    ganadas = []
    ganadas.append(Actividad("coleccion datos", "01/02/20", "Escanear temperaturas"))
    ganadas.append(Actividad("entrevistas", "01/02/20", "entrevista con cliente"))
    return ganadas


def ganadas():
    ganadas = []
    return ganadas
