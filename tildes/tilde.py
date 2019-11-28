palabras = {"Teclado": 13, "Raton": 9, "Impresora": 35, "Escaner": 25}

palabrasTildes = {"á": 'a', "é": 'e', "í": 'i', "ó": 'o', "ú": 'u'}

opcion = input("Periferico: ")
opcionNueva =""

for i in opcion:

    if palabrasTildes.get(i) is not None:
        opcionNueva += palabrasTildes.get(i)
    else:
        opcionNueva += i

correcto = palabras.get(opcionNueva)

if correcto is not None:
    print("Precio del ", opcionNueva, "-->", correcto)
else:
    print("No se ha encontrado")

