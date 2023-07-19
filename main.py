import requests
import json


# request sencillo
"""url = "https://rickandmortyapi.com/api/character/2" # se consume la url
r = requests.get(url) # metodo para obtener HTTP 

response = r.text # Para obtener la respuesta tipo texto
print(response) # Solo se imprime

j = r.json() # se parce a JSON para poder acceder al diccionario.
print(j.keys()) # Solo se imprime las llaves del diccionario.

status = j["status"] # Se impirme solo el valor de esa llave que es status
print(status)
"""
"""i = 1

while i < 10:
    url = "https://rickandmortyapi.com/api/character/{}".format(i)
    r = requests.get(url)

    j = r.json()
    name = j["name"] # accede al nombre de la llave
    status = j["status"] # accede al estatus

    print(" El nombre {} y el status {}".format(name, status)) # Se imprime el nombre y el status de los primeros 10 personajes de la seris.
    i += 1 # se auto incrementa para que se realice el ciclo.
"""

# reques al primer episodio
url = "https://rickandmortyapi.com/api/episode/1"
r = requests.get(url) # Se solicita mediante en request de la URL, en la variable de r, para su parce.

j = r.json() # Se convierte en un lista JSON.
personajes = j["characters"] # Se extrae del Json una lista que se almacena en la variable personajes
list_name_human = list() # Se crean listas vacias para almacenas los datos
list_name_other = list()

for personaje in personajes:
    req = requests.get(personaje)
    j = req.json()
    specie = j["species"]  # Extraer la especie de todos de el json
    name = j["name"] # Extraer el nombre de todos el en JSON
    
    if j["species"] == "Human":
        list_name_human.append(name)
    else:
        list_name_other.append(name)
    

print(list_name_human)
print(list_name_other)





