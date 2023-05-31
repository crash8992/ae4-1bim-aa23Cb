from dataBpaises import client

db = client.dataBpaises01
coleccion2 = db.colpaises01

nombre_pais = input("ingrese el nombre del pais: ")
continente = input("ingrese nombre continente: ")
hab_pais = float(input("ingrese # millones habitantes: "))


if hab_pais > 50:
    estado_poblacion = "Altamente Poblado"
else:
    estado_poblacion = "medianamente poblado"

datos2 ={"nombre_pais": nombre_pais, "continente": continente, "habitantesPaís": hab_pais, "estadoPoblación": estado_poblacion}

coleccion2.insert_one(datos2)

