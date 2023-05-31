from dataBciudad import client

db = client.dataBase01
coleccion1 = db.cuidades

filter = {"pais ciudad":{"$eq": "Ecuador"}}
results2 = coleccion1.find(filter)

for registro02 in results2:
    print(registro02)