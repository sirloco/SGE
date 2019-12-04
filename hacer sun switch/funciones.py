def multiplicar(n1,n2):
    print(n1, "X", n2, "=", n1*n2)

def sumar(n1,n2):
    print(n1, "+", n2, "=", n1+n2)

def resta(n1,n2):
    print(n1, "-", n2, "=", n1-n2)

def division(n1,n2):
    print(n1, "/", n2, "=", n1/n2)

funciones = {1: multiplicar,2: sumar,3: resta,4: division}

opcion = -1
while opcion != 5:
    n1 = int(input("Escribe un número: "))
    n2 = int(input("Escribe otro número: "))

    print("1.- multiplica\n"
        "2.- suma\n"
        "3.- resta\n"
        "4.- divide\n"
        "5.- salir")
    opcion = int(input("opcion: "))

    if opcion !=5:
        funciones.get(opcion)(n1, n2)

