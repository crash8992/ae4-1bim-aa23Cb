from dataBpaises import client

db = client.dataBpaises01
coleccion2 = db.colpaises01

print("mostrar todos los paises")
datos2 = coleccion2.find()

for  regsitro2 in datos2:
    print(regsitro2)