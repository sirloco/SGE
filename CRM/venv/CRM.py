import Clase

clientes = []
oportunidades = []

def muestraOportunidad():
    repite = True
    while repite:
        i = 1
        for o in oportunidades:
            print(i, ": ", o.getNombre())
            i += 1

        try:
            return int(input("Elige una oportunidad: "))-1
        except:
            repite = True


def creaActividad():

    nombre = ""
    fecha = ""
    descripcion = ""
    if len(oportunidades) < 1:
        print("Debe existir una Oportunidad para una actividad")
    else:
        opor = muestraOportunidad()

        repite = True
        while repite:
            nombre = input("Nombre de Actividad: ")
            fecha = input("Fecha: ")
            descripcion = input("Descripción: ")

            if nombre == "" or fecha == "" or descripcion == "":
                print("Campos obligatorios!\n")
                repite = True
            else:
                repite = False

        #creamos actividad
        actividad = Clase.Actividad(nombre,descripcion,fecha)
        #añadimos la actividad a la lista de nuevas actividades de la oportunidad selecionada
        oportunidades[opor].getNuevas().append(actividad)
        #le indicamos a la actividad a que oportunidad pertenece
        actividad.setOportunidad(oportunidades[opor])



def cambiaEstado():
    return "Cambia estado"

def creaOportunidad():
    repite = True
    while repite:
        nombre = input("Nombre: ")

        if nombre == "":
            print("Campos obligatorios!\n")
            repite = True
        else:
            repite = False

        oportunidad = Clase.Oportunidad(nombre)

        oportunidades.append(oportunidad)

        print("{0} Creada!\n".format(oportunidad.getNombre()))


def creaCliente():

    nombre = ""
    empresa = ""
    repite = True
    while repite:
        nombre = input("Nombre de cliente: ")
        empresa = input("Empresa que pertenece: ")

        if nombre == "" or empresa == "":
            print("Campos obligatorios!\n")
            repite = True
        else:
            repite = False


    cliente = Clase.Cliente(nombre, empresa)

    clientes.append(cliente)

    print("{0} Creado!\n".format(cliente.getNombre()))


#//////////////////////////////////////////////////////////////////////////////////////

opciones = {"1": creaOportunidad, "2": creaCliente, "3": creaActividad, "4": cambiaEstado}

opcion = "0"
while opcion != "5":

    print("1.- Crear Oportunidad\n"
          "2.- Crear Cliente\n"
          "3.- Crear Actividad\n"
          "4.- Cambiar estado Actividad\n"
          "5.- Salir")

    opcion = input("opcion: ")[0]

    if opcion != "5":
        opciones.get(opcion)()







#print("Nombre {0} empresa {1}".format(clientes[0].getNombre(), clientes[0].getEmpresa()))