from dataBciudad import client

db = client.dataBase01
coleccion1 = db.cuidades

print("mostrar todas las ciudades")
datos1 = coleccion1.find()
for registro1 in datos1:
    print(registro1)