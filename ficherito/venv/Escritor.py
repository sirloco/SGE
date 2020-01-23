from datetime import datetime

archivo = open("log.txt", "a")

ahora = datetime.now()

archivo.writelines(("Accedido " + ahora.strftime("%d-%m-%Y (%H horas :%M minutos :%S segundos")+ "\n" ))

archivo.close()