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
