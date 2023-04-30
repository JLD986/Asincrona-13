#Definir una función que pregunte al usuario si desea ejecutar el programa

def ejecutar_programa():


    respuesta = input("¿Desea ejecutar el programa? (S/N): ")

    if respuesta.upper() == "S":
# Definir una lista de nombres de integrantes del grupo
        nombres = ["Lisandro", "Xavier", "Fatima", "Edgar"]

# Mostrar el menú de nombres
        print("Seleccione el nombre del integrante del grupo:")
        for i in range(len(nombres)):
 
            print(str(i+1) + ". " + nombres[i])
# Pedir al usuario que ingrese el nombre del integrante
        while True:
            nombre_elegido = input("Ingrese el nombre del integrante: ")
            nombres = ["Lisandro", "Xavier", "Fatima", "Edgar"]
            if nombre_elegido not in nombres:
             input("Ingrese otro nombre, este no esta en labase de datos: ")
            else: break
            
# Definir un diccionario con los datos de los integrantes del grupo
        datos_integrantes = {
            "Lisandro": {"nombres": " Jose Lisandro ", "apellidos": "Ramos Dominguez", "sexo": "Masculino", "edad": 19, "departamento": "Chalatenango", "municipio": " Concepcion quezaltepeque ", "dirección": "El sur de california papa"},
            "Fatima": {"nombres": "Fatima Estefany ", "apellidos": "Rivas Lopez", "sexo": "Femenino", "edad": 18, "departamento": "Chalatenango", "municipio": "por ahi ", "dirección": "Donde la luz del sol no llega"},
            "Xavier": {"nombres": " Xavier Ernesto ", "apellidos": " Rivera Gonzales ", "sexo": "Masculino", "edad": 17, "departamento": "Cuscatlan ", "municipio": "Suchitoto", "dirección": "Calle 8, Johannesburgo Sudafrica"},
            "Edgar": {"nombres": "Edgar Rene ", "apellidos": "Rivas Castro", "sexo": "si porfavor", "edad": 24, "departamento": "Lima", "municipio": "San Borja", "dirección": "Av. Aviación 1010"}
                }
# Verificar si el nombre elegido está en la lista de nombres
        if nombre_elegido in nombres:
# Mostrar los datos del integrante correspondiente

         print("Nombres: " + datos_integrantes[nombre_elegido]["nombres"])

         print("Apellidos: " + datos_integrantes[nombre_elegido]["apellidos"])

         print("Sexo: " + datos_integrantes[nombre_elegido]["sexo"])

         print("Edad: " + str(datos_integrantes[nombre_elegido]["edad"]))

         print("Departamento: " + datos_integrantes[nombre_elegido]["departamento"])

         print("Municipio: " + datos_integrantes[nombre_elegido]["municipio"])

         print("Dirección: " + datos_integrantes[nombre_elegido]["dirección"])
# Preguntar al usuario si desea consultar otro dato
         sndrespuesta = input("¿Desea consultar otro dato? (S/N): ")
         if sndrespuesta.upper() == "s":

            ejecutar_programa()

        else:
            print("Programa finalizado.")

ejecutar_programa()

print("FIN")