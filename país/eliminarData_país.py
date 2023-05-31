from dataBpaises import client

db = client.dataBpaises01
coleccion2 = db.colpaises01

print("mostrar todas las ciudades")
datos1 = coleccion2.find()
for registro3 in datos1:
    print(registro3)

print("Eliminar elemento en base ciudades")
coleccion2.delete_many({'habitantesPaís': 1})