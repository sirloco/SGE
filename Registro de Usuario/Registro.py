import string
import random

listaNombres = ["Santi", "Fulano", "Mengano", "Zutano"]

def mostrarNombres():
    print("////////////// Listado ///////////////")
    for j in listaNombres:
        print(j)
    print("//////////////////////////////////////")


def generar(opciones):
    con = ""
    #todo preguntar como se puede partir el if que se me sale de la linea
    if opciones['b'] == "Excluir" and opciones['c'] == "Excluir" and opciones['d'] == "Excluir" and opciones['e'] == "Excluir":
        print("Has desactivado todas las opciones así que te quedas sin contraseña")
    else:
        while True:#se va metiendo caracter a caracter hasta tener el tope aunque me paso por uno
            if opciones['b'] == "Incluir" and len(con) <= opciones['a']:
                con += random.choice(string.ascii_lowercase)
            if opciones['c'] == "Incluir" and len(con) <= opciones['a']:
                con += random.choice(string.ascii_uppercase)
            if opciones['d'] == "Incluir" and len(con) <= opciones['a']:
                con += random.choice(string.punctuation)
            if opciones['e'] == "Incluir" and len(con) <= opciones['a']:
                con += random.choice(string.digits)
            #rectifico lo que me sobra y salgo del bucle
            if len(con) >= opciones['a']:
                con = con[:opciones['a']]
                break


    return con


# ///////////////////////////// PARTE 1 /////////////////////////////////////////
mostrarNombres()

while True:
    # en cada vuelta es importante inicializar la variable de los errores
    errores = ""
    nombre = input("Añade un nombre: ")
    # bucle para ver si el nombre está en la lista el break no afecta al while<-- IMPORTANTE
    for i in listaNombres:
        if i == nombre.capitalize():
            errores = "El nombre ya esxiste en la lista prueba otro 😉"
            break
    # comprobación de errores
    if errores:
        print(errores)
    else:
        listaNombres.append(nombre.capitalize())
        mostrarNombres()
        break

# ///////////////////////////// PARTE 2 /////////////////////////////////////////
opciones = dict.fromkeys(['b', 'c', 'd', 'e'], "Incluir")
opciones.setdefault('a', 8)#aquí no sabia como meterlo al principio//todo preguntar como hacerlo bien
opcion = ""
contrasinal = ""
while opcion.lower() != 'f':
    #Muestra el menú con las opciones todas en incluir
    opcion = input("a) Definir Longitud de Contraseña\n"
                   "b) " + opciones.get('b') + " Minúsculas\n"
                    "c) " + opciones.get('c') + " Mayúsculas\n"
                    "d) " + opciones.get('d') + " Símbolos\n"
                    "e) " + opciones.get('e') + " Números\n"
                    "f) Generar\n"
                    "Opción: ")[0]#para coger solo el primer digito (aunque luego se controla en el else)

    #cambia de una a otra segun le vas dando a las opciones
    if opcion == 'a':
        opciones['a'] = int(input("Escribe tamaño de la contraseña: "))
    elif opcion == 'b':
        opciones['b'] = "Excluir" if opciones.get('b') == "Incluir" else "Incluir"#el == devuelve True o False
    elif opcion == 'c':
        opciones['c'] = "Excluir" if opciones.get('c') == "Incluir" else "Incluir"
    elif opcion == 'd':
        opciones['d'] = "Excluir" if opciones.get('d') == "Incluir" else "Incluir"
    elif opcion == 'e':
        opciones['e'] = "Excluir" if opciones.get('e') == "Incluir" else "Incluir"
    elif opcion == 'f':
        contrasinal = generar(opciones)
    else:
        print("Opción Incorrecta 🤬\n")

# ///////////////////////////// PARTE 3 /////////////////////////////////////////

print(contrasinal)