def multiplicar():
    print ("tabla")

funciones = {1: multiplicar}

opcion = int(input("opcion: "))

funciones.get(opcion)()

