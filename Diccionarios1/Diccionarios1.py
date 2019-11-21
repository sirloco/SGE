perifericos = {"Teclado":13, "Raton":9, "Impresora":35, "Escaner":25}
p = input("Escribe Periférico: ")
correcto = perifericos.get(p)

if correcto is not None:
    print("Precio del ", p, "-->", correcto)
else:
    print("No se ha encontrado")