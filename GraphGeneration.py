import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
nodos=1500
# Cargamos los datos
data = pd.read_csv('dataset.csv', nrows=nodos)

# Crear un grafo vacío
G = nx.Graph()

# Generar diccionarios de mapeo
actor_dict = {}
genre_dict = {}
director_dict = {}
counter = 0

# Función para mapear y obtener el código numérico de una entidad
def obtener_codigo(entidad, entidad_dict):
    global counter  # Declarar counter como global
    if entidad == '' or entidad == '-':
        return -1
    if entidad not in entidad_dict:
        entidad_dict[entidad] = counter
        counter += 1
    return entidad_dict[entidad]

# Iterar sobre los datos y agregar nodos al grafo
for _, row in data.iterrows():
    id_ = row['id']
    G.add_node(id_)

# Iterar nuevamente para agregar aristas ponderadas basadas en similitud
for i, row_i in data.iterrows():
    for j, row_j in data.iterrows():
        if i != j:
            id_i = row_i['id']
            id_j = row_j['id']

            # Mapeo de entidades a códigos numéricos
            director_i = obtener_codigo(row_i['director'], director_dict)
            director_j = obtener_codigo(row_j['director'], director_dict)
            actors_i = [obtener_codigo(actor, actor_dict) for actor in row_i['actors'].split(', ')]
            actors_j = [obtener_codigo(actor, actor_dict) for actor in row_j['actors'].split(', ')]
            genres_i = [obtener_codigo(genre, genre_dict) for genre in row_i['genres'].split(', ')]
            genres_j = [obtener_codigo(genre, genre_dict) for genre in row_j['genres'].split(', ')]

            # Calcular la similitud basada en tus criterios
            peso = 0
            if row_i['duration'] != -1 and row_i['duration'] == row_j['duration']:
                peso += 1
            if director_i != -1 and director_j != -1 and director_i == director_j:
                peso += 5
            peso += sum(1 for actor_code in actors_i if actor_code != -1 and actor_code in actors_j)
            peso += sum(5 for genre_code in genres_i if genre_code != -1 and genre_code in genres_j)
            if row_i['year'] != -1 and row_i['year'] == row_j['year']:
                peso += 1

            if peso > 2:
                similarity = 100 / peso
                G.add_edge(id_i, id_j, weight=peso)

# Dibujo del grafo
nx.draw(G, with_labels=False, node_size=5, node_color='black')

# Mostrar la ventana
plt.show()
