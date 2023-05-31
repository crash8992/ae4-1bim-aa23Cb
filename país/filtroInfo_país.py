from dataBpaises import client

db = client.dataBpaises01
coleccion2 = db.colpaises01

filter = {"habitantesPaís": {"$lt": 50}}
results = coleccion2.find(filter)
for registro4 in results:
    print(registro4)
