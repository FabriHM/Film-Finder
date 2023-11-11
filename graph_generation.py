import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 2000

# Load the data
data = pd.read_csv('dataset.csv', nrows=num_nodes)

# Create dictionaries to map actors, genres, and directors to numerical values
actor_dict = {}
genre_dict = {}
director_dict = {}
counter = 0

processed_data = []
for _, row in data.iterrows():
    actors = row['actors'].split(', ')
    genres = row['genres'].split(', ')
    director = row['director']

    actor_codes = []
    # Map actors to numerical values
    for actor in actors:
        if actor == '' or actor == '-':
            actor_codes.append(-1)
        else:
            if actor not in actor_dict:
                actor_dict[actor] = counter
                counter += 1
            actor_codes.append(actor_dict[actor])

    genre_codes = []
    # Map genres to numerical values
    for genre in genres:
        if genre == '' or genre == '-':
            genre_codes.append(-1)
        else:
            if genre not in genre_dict:
                genre_dict[genre] = counter
                counter += 1
            genre_codes.append(genre_dict[genre])

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
    movie_values = [id_, duration, director_code, actor_codes, genre_codes, row['year']]
    processed_data.append(movie_values)

G = nx.Graph()
# Generate the adjacency matrix
adjacency_matrix = np.full((num_nodes, num_nodes), 0)

# Add nodes to the graph
for movie in processed_data:
    G.add_node(movie[0])

# Add edges to the graph with their respective weights
for i in range(len(processed_data)):
    for j in range(i + 1, len(processed_data)):
        weight = 0
        # Calculate weights based on various conditions
        if processed_data[i][1] == processed_data[j][1] and processed_data[i][1] != -1:
            weight += 1
        if processed_data[i][2] == processed_data[j][2] and processed_data[i][1] != -1:
            weight += 5
        for actor_i in processed_data[i][3]:
            for actor_j in processed_data[j][3]:
                if actor_i == actor_j and actor_i != -1:
                    weight += 1
        for genre_i in processed_data[i][4]:
            for genre_j in processed_data[j][4]:
                if genre_i == genre_j and genre_i != -1:
                    weight += 5
        if processed_data[i][5] == processed_data[j][5] and processed_data[i][1] != -1:
            weight += 1
        # Consider only edges with weight greater than 2
        if weight > 2:
            similarity = 100 / weight
            adjacency_matrix[processed_data[j][0]][processed_data[i][0]] = weight
            adjacency_matrix[processed_data[i][0]][processed_data[j][0]] = weight
            G.add_edge(processed_data[i][0], processed_data[j][0], weight=weight)


# Print the adjacency matrix to a CSV file
df = pd.DataFrame(adjacency_matrix)
df.to_csv('matrizAdy.csv', index=False, header=False) 

pos = nx.spring_layout(G, seed=42) 
labels = {node: str(node) for node in G.nodes} 

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=False, node_size=5, node_color='black', font_size=8, font_color='white', font_weight='bold', edge_color='gray', alpha=0.5)

#Add IDs of movies
for node, (x, y) in pos.items():
    plt.text(x, y, str(node), fontsize=6, ha='center', va='center', color='blue', bbox=dict(facecolor='white', alpha=0.5, edgecolor='white', boxstyle='round,pad=0.3'))

plt.title('Graph of Movie Recomendation with IDs', fontsize=14)
plt.show()
