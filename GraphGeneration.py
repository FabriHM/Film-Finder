import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

nodes = 2000

# Load the data
data = pd.read_csv('dataset.csv', nrows=nodes)

# Create dictionaries to map actors, genres, and directors to numerical values
actor_dict = {}
genre_dict = {}
director_dict = {}
counter = 0

data2 = []
for _, row in data.iterrows():
    actors = row['actors'].split(', ')
    genres = row['genres'].split(', ')
    director = row['director']

    actors_codes = []
    # Map actors to numerical values
    for actor in actors:
        if actor == '' or actor == '-':
            actors_codes.append(-1)
        else:
            if actor not in actor_dict:
                actor_dict[actor] = counter
                counter += 1
            actors_codes.append(actor_dict[actor])

    genres_codes = []
    # Map genres to numerical values
    for genre in genres:
        if genre == '' or genre == '-':
            genres_codes.append(-1)
        else:
            if genre not in genre_dict:
                genre_dict[genre] = counter
                counter += 1
            genres_codes.append(genre_dict[genre])

    if director == '' or director == '-':
        director_code = -1
    else:
        if director not in director_dict:
            director_dict[director] = counter
            counter += 1
        director_code = director_dict[director]

    id_ = row['id']
    duration = row['duration']

    # Create the list of numerical values for the current movie
    movie_values = [id_, duration, director_code, actors_codes, genres_codes, row['year']]
    data2.append(movie_values)

G = nx.Graph()
# Generate the adjacency matrix
adjacency_matrix = np.full((nodes, nodes), 0)

# Add nodes to the graph
for movie in data2:
    G.add_node(movie[0])

# Add edges to the graph with their respective weights
for i in range(len(data2)):
    for j in range(i + 1, len(data2)):
        weight = 0
        # Calculate weights based on various conditions
        if data2[i][1] == data2[j][1] and data2[i][1] != -1:
            weight += 1
        if data2[i][2] == data2[j][2] and data2[i][1] != -1:
            weight += 5
        for actor_i in data2[i][3]:
            for actor_j in data2[j][3]:
                if actor_i == actor_j and actor_i != -1:
                    weight += 1
        for genre_i in data2[i][4]:
            for genre_j in data2[j][4]:
                if genre_i == genre_j and genre_i != -1:
                    weight += 5
        if data2[i][5] == data2[j][5] and data2[i][1] != -1:
            weight += 1
        # Consider only edges with a weight greater than 2
        if weight > 2:
            similarity = 100 / weight
            adjacency_matrix[data2[j][0]][data2[i][0]] = weight
            adjacency_matrix[data2[i][0]][data2[j][0]] = weight
            G.add_edge(data2[i][0], data2[j][0], weight=weight)

# Print the adjacency matrix to a CSV file
df = pd.DataFrame(adjacency_matrix)
df.to_csv('matrizAdy.csv', index=False, header=False)

# Draw the graph using NetworkX and Matplotlib
nx.draw(G, with_labels=False, node_size=5, node_color='black')
plt.show()
