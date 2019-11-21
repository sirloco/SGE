diccionario = {}

def muestra(diccionario):
    for clave,valor in dicionario.items():
        print("Clave:", clave, "--> Valor: ", valor)


print("Diccionario creado con dict")
dicionario = dict(a=1, b=2, c=3)
muestra(diccionario)


print("Limpiado Diccionario con clear")
diccionario.clear()

print("Diccionario creado con dict y zip")
diccionario = dict(zip('abc', [1, 2, 3]))
muestra(diccionario)

print("Obtener claves con keys()")
for clave in diccionario.keys():
    print(clave)

print("Obtener valores con values()")
for valores in diccionario.values():
    print(valores)

print("Hacer copia del diccionario con copy()")
copiaDiccionario = diccionario.copy()
muestra(copiaDiccionario)

print("Asignar a todos las claves el mismo valor")
dicionario = dict.fromkeys(['a', 'b', 'c'], 0)
muestra(diccionario)

print("Obtener valor con get() --> b valor ", dicionario.get('b'))

print("Eliminar un elemento del diccionario pop()")
dicionario.pop('b')
muestra(dicionario)

print("Muestra el valor de la clave con setdefault() a valor ", dicionario.setdefault('a'))

print("Sobrescribe el diccionario original con la copia con update()")
dicionario.update(copiaDiccionario)

muestra(dicionario)









