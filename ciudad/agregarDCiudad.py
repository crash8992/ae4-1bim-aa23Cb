from dataBciudad import client

db = client.dataBase01
coleccion1 = db.cuidades

nombre_ciudad = input("ingrese el nombre de la ciudad: ")
pais_ciudad = input("ingrese el país donde se encuentra: ")
hab_ciudad = float(input("ingrese # en millones "))
capital = input("¿La ciudad es capital del país: ")

if capital.lower() == "SI":
    is_capital = True
else:
    is_capital = False


datos1 = {"nombre ciudad": nombre_ciudad, "pais ciudad": pais_ciudad, "habitantes": hab_ciudad, "capital": capital }

coleccion1.insert_one(datos1) 

