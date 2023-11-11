import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import mpl_toolkits as mpl

def get_reachable_nodes(adjacency_matrix, labels, node):
    n = len(adjacency_matrix)
    visited = [False] * n
    reachable_nodes = []
    
    stack = [node]
    visited[node] = True
    
    while stack:
        v = stack.pop()
        reachable_nodes.append(labels[v])
        
        for i in range(n):
            if adjacency_matrix[v][i] != 0 and not visited[i]:
                stack.append(i)
                visited[i] = True
    
    return reachable_nodes

def get_subgraph(adjacency_matrix, node_list, node):
    subgraph_nodes = [n for n in node_list if n != node]
    if node is not None:
        subgraph_nodes.insert(0, node)  # Insert the node of interest at the first position
    
    subgraph_matrix = [[adjacency_matrix[i][j] for j in subgraph_nodes] for i in subgraph_nodes]
    
    return subgraph_matrix, subgraph_nodes

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movie Suggestions")
        self.geometry("1200x600")

        self.label_movie = tk.Label(self, text="Enter the name of the movie:")
        self.label_movie.place(x=20, y=45)

        self.label_1 = tk.Label(self, text="Director:")
        self.label_1.place(x=900, y=45)

        self.label_2 = tk.Label(self, text="Genre:")
        self.label_2.place(x=600, y=45)

        self.entry_movie = tk.Entry(self)
        self.entry_movie.place(x=250, y=45)

        self.button_update = tk.Button(self, text="Suggestions", command=self.make_suggestion)
        self.button_update.place(x=450, y=40)

        # Create a table
        self.table = ttk.Treeview(self, columns=("ID", "Name", "Director", "Genre", "Duration(mins)"), show="headings")
        self.table.column("ID", width=50)
        self.table.column("Name", width=150)
        self.table.column("Director", width=150)
        self.table.column("Genre", width=150)
        self.table.column("Duration(mins)", width=50)

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Director", text="Director")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Duration(mins)", text="Duration(mins)")

        # Create a scrollbar and associate it with the table
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)

        # Position the table and scrollbar in the window
        self.table.place(x=550, y=100, width=600, height=450)
        scrollbar.place(x=1150, y=100, height=450)

        # Read the CSV file and store it in a DataFrame
        df = pd.read_csv('dataset.csv')

        # Convert the DataFrame to an array of objects
        self.data = df.to_dict('records')

        # Get a list of unique directors
        self.directors = df['director'].unique().tolist()

        # Get a list of unique genres (separated by ',')
        self.genres = df['genres'].str.split(',').explode().apply(lambda x: x.strip()).unique().tolist()

        # Create the genres combobox
        self.combo_genres = ttk.Combobox(self)
        self.combo_genres['values'] = self.genres
        self.combo_genres.place(x=690, y=45)

        # Create the directors combobox
        self.combo_directors = ttk.Combobox(self)
        self.combo_directors['values'] = self.directors
        self.combo_directors.place(x=990, y=45)

        # Load the adjacency matrix
        self.matrix = np.loadtxt('matrizAdy.csv', delimiter=',')

        # Create an example graph
        self.update_graph()

    def make_suggestion(self):
        self.update_graph()

    # LINEAR SEARCH
    def search_movie(self, movie_name):
        movie = None
        for item in self.data:
            if item['title'] == movie_name:
                movie = item
                break
            try:
                if item['id'] == int(movie_name):
                    movie = item
                    break
            except ValueError:
                pass
        return movie

    def update_table(self, movie_list):
        # Clear the table
        self.table.delete(*self.table.get_children())

        # Find objects with ID equal to the elements in the list
        for i in movie_list:
            # Add the object to the table
            item = self.data[i]
            self.table.insert("", "end", values=(item['id'], item['title'], item['director'], item['genres'], item['duration']))

    def apply_constraint(self, director, genre, movie_list):
        sublist = []
        if director and director != "" and director != "-" and genre and genre != "" and genre != "-":
            for i in movie_list:
                obj = self.data[i]
                if obj["director"] == director and genre in obj["genres"]:
                    sublist.append(i)

        elif director and director != "" and director != "-":
            for i in movie_list:
                obj = self.data[i]
                if obj["director"] == director:
                    sublist.append(i)
        
        elif genre and genre != "" and genre != "-":
            for i in movie_list:
                obj = self.data[i]
                if genre in obj["genres"]:
                    sublist.append(i)
        else:
            for i in movie_list:
                sublist.append(i)

        return sublist

   

if __name__ == "__main__":
    # This block will only be executed if the script is run directly, not if it is imported as a module
    main_window = MainWindow()
    main_window.mainloop()
