import Clase

clientes = []
oportunidades = []


# /////////////// MUESTRA LISTADO DE OPORTUNIDADES DEVUELVE ELEGIDA///////////////////
def muestraOportunidad():
    repite = True
    while repite:
        i = 1
        for o in oportunidades:
            print(i, ": ", o.getNombre())
            i += 1

        try:
            return int(input("Elige una oportunidad: ")) - 1
        except:
            repite = True


#################################################################################

# ////////////////// CREA ACTIVIDAD Y LA ENLAZA CON SU OPORTUNIDAD ///////////////
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

        # creamos actividad
        actividad = Clase.Actividad(nombre, descripcion, fecha)
        # añadimos la actividad a la lista de nuevas actividades de la oportunidad selecionada
        oportunidades[opor].getActividades().append(actividad)
        # le indicamos a la actividad a que oportunidad pertenece
        actividad.setOportunidad(oportunidades[opor])


#######################################################################################

# ///////////////////////////////////// CAMBIA ACTIVIDAD DE ETAPA /////////////////////
def cambiaEtapa():
    if len(oportunidades) < 1:
        print("Debe existir una Oportunidad para una actividad")
    else:

        acti = -1
        etap = -1
        opor = muestraOportunidad()

        repite = True
        while repite:
            i = 1
            for actividad in oportunidades[opor].getActividades():
                print(i, ": ", actividad.getNombre())
                i += 1
            try:
                acti = int(input("Elige una Actividad: ")) - 1
                repite = False
            except:
                repite = True

        repite = True
        while repite:
            print("-Etapas disponibles-\n"
                  "1.- Nueva\n"
                  "2.- Calificada\n"
                  "3.- Propuesta\n"
                  "4.- Ganada")
            try:
                etap = int(input("Elige una Etapa: ")) - 1
                repite = False
            except:
                repite = True

        oportunidades[opor].getActividades()[acti].setEtapa(etap)
        print("Etapa cambiada!")


#######################################################################################

# ///////////////////////////////////// CREA OPORTUNIDAD /////////////////////////////////
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


####################################################################################

# ///////////////// LISTADO DE LAS ACTIVIDADES DE UNA OPRTUNIDAD////////////////////
def mostrarActividades():

    if len(oportunidades) > 0:
        opor = muestraOportunidad()

        if len(oportunidades[opor].getActividades()) > 0:
            for actividad in oportunidades[opor].getActividades():
                print("\nNombre: ", actividad.getNombre())
                print("Fecha: ", actividad.getFecha())
                print("Descripción: ", actividad.getDescripcion())
                print("Estado: ", actividad.getEtapa())

        else:
            print("En esta oportunidad no existe ninguna actividad")
    else:
        print("Debe existir al menos una oportunidad")

####################################################################################

# ///////////////////////////////////// CREA CLIENTE/////////////////////////////////
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


#####################################################################################

# ///////////////////// ENLAZA UN CLIENTE CON UNA OPORTUNIDAD //////////////////////
def apuntaCliente():
    if len(oportunidades) < 1 or len(clientes) <1:
        print("Debe esxistir al menos una oportunidad y un cliente")
    else:
        cli = ""
        repite = True
        while repite:
            i = 1

            for cli in clientes:
                print(i, ": ", cli.getNombre())
                i += 1

            try:
                c = int(input("Elige un Cliente: ")) - 1
                repite = False
            except:
                repite = True

        opor = muestraOportunidad()

        cli.setOportunidad(oportunidades[opor])

        print(cli.getNombre(), " apuntado a ", oportunidades[opor].getNombre())


####################################################################################

# ///////////////////// ELIMINA UNA OPORTUNIDAD SELECCIONADA ///////////////////////
def eliminarOportunidad():

    if len(oportunidades) < 1:
        print("Debe esxistir al menos una oportunidad")
    else:

        opor = muestraOportunidad()

        for cli in clientes:
            if (cli.getOportunidad() == oportunidades[opor].getNombre()):
                cli.setOportunidad = ""

        oportunidades[opor].getActividades().clear()
        oportunidades.pop(opor)

        print("Eliminada!")


####################################################################################

# /////////////////////////////////////// GRAFICOS /////////////////////////////////
def grafico():
    print("crea un grafico")


####################################################################################

# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// MENU ///////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
opciones = {"1": creaOportunidad, "2": creaCliente, "3": creaActividad, "4": apuntaCliente, "5": cambiaEtapa,
            "6": mostrarActividades, "7": eliminarOportunidad, "8": grafico}

opcion = "0"
while opcion != "9":

    print("1.- Crear Oportunidad\n"
          "2.- Crear Cliente\n"
          "3.- Crear Actividad\n"
          "4.- Apuntar cliente a una Oportunidad\n"
          "5.- Cambiar etapa Actividad\n"
          "6.- Mostrar actividades de una oportunidad\n"
          "7.- Elminar Oportindad\n"
          "8.- Graficos\n"
          "9.- Salir")

    opcion = input("opcion: ")[0]

    if opcion != "9":
        opciones.get(opcion)()
