nombre = input("Escribe un nombre: ")

errores = "El nombre de usuario no puede contener más de 12 caracteres\n" if len(nombre) > 12 else ""

errores += "El nombre de usuario debe contener al menos 6 caracteres\n" if len(nombre) < 6 else ""

errores += "El nombre de usuario puede contener solo letras y números\n" if not nombre.isalnum() else ""

print(errores if len(errores) > 0 else "True")
