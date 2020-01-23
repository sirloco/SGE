import Clase

nombre = input("Nombre Cliente: ")
empresa = input("Nombre Empresa: ")

cliente = Clase.Cliente(nombre, empresa)



print(cliente.nombre)
print(cliente.Oportunidad()[0])
