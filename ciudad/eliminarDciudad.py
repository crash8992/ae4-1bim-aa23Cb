from dataBciudad import client

db = client.dataBase01
coleccion1 = db.cuidades

print("mostrar todas las ciudades")
datos1 = coleccion1.find()
for registro2 in datos1:
    print(registro2)

print("Eliminar elemento en base ciudades")
coleccion1.delete_many({'habitantes': 18})