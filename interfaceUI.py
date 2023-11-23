import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import messagebox
from collections import deque
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import mpl_toolkits as mpl
import matplotlib.cm as cm

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
        self.configure(bg='black')
        self.tk_setPalette(background='#2E2E2E', foreground='white')
        label_font = ('Montserrat', 10)
        self.title("Movie Suggestions")
        self.geometry("1280x600")

        style = ttk.Style(self)
        
        style.theme_create("custom_theme", parent="alt", settings={
            "TCombobox": {
                "configure": {"selectbackground": 'white', "fieldbackground": '#2E2E2E', "foreground": 'white'},
            }
        })

        style.theme_use("custom_theme")

        self.label_movie = tk.Label(self, text="Enter the name of the movie:", fg='white', bg = 'black', font=label_font)
        self.label_movie.place(x=20, y=45)

        self.label_1 = tk.Label(self, text="Director:", fg='white', bg = 'black', font=label_font)
        self.label_1.place(x=900, y=45)

        self.label_2 = tk.Label(self, text="Genre:", fg='white', bg = 'black', font=label_font)
        self.label_2.place(x=600, y=45)

        self.entry_movie = tk.Entry(self)
        self.entry_movie.place(x=250, y=45)

        self.button_update = tk.Button(self, text="Suggestions", command=self.make_suggestion, fg='white', bg = 'blue', font=label_font)
        self.button_update.place(x=450, y=40)

        # Create a table
        self.table = ttk.Treeview(self, columns=("ID", "Name", "Director", "Genre", "Duration(mins)"), show="headings", style="mystyle.Treeview")
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

        # Table of users
        self.table_users = ttk.Treeview(self, columns=("Name"), show="headings", style="mystyle.Treeview")
        self.table_users.column("Name", width=150)
        self.table_users.heading("Name", text="Name")

        # Create a scrollbar and associate it with the table
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)

        # Position the table and scrollbar in the window
        self.table.place(x=20, y=100, width=600, height=450)
        scrollbar.place(x=620, y=100, height=450)
        self.table_users.place(x=1050, y=100, width=200, height=450)

        # Read the CSV file and store it in a DataFrame
        df = pd.read_csv('dataset.csv')
        # Read the CSV file and store it in a DataFrame
        df1 = pd.read_csv('users.csv', usecols=['MovieFavorite'])

        # Convert the DataFrame to an array of objects
        self.data = df.to_dict('records')

        # Get a list of unique directors
        self.directors = df['director'].unique().tolist()

        # Get a list of unique genres (separated by ',')
        self.genres = df['genres'].str.split(',').explode().apply(lambda x: x.strip()).unique().tolist()

         # Create the genres combobox
        self.combo_genres = ttk.Combobox(self, style="custom_theme.TCombobox")
        self.combo_genres['values'] = self.genres
        self.combo_genres.place(x=655, y=45)

        # Create the directors combobox
        self.combo_directors = ttk.Combobox(self, style="custom_theme.TCombobox")
        self.combo_directors['values'] = self.directors
        self.combo_directors.place(x=965, y=45)

        # Load the adjacency matrix
        self.matrix = np.loadtxt('matrizAdy.csv', delimiter=',')
        
        # Create an example graph
        self.update_graph()

    def make_suggestion(self):
        self.update_graph()

   # BFS  Algorithm
    def search_movie_bfs(self, movie_name):
        # 1. Initialization of the queue and the set of visited nodes
        queue = deque(self.data)
        visited = set()

        # 2. Main loop
        while queue:
            # 3. Visit condition
            item = queue.popleft()
            if item['id'] in visited:
                continue

            # 4. Mark as visited
            visited.add(item['id'])

            # 5. Search condition
            if item['title'] == movie_name or (isinstance(movie_name, int) and item['id'] == movie_name):
                # 6. Return if the movie is found
                return item

            # 7. Expansion of neighboring nodes
            try:
                queue.extend(self.data[int(movie_name):])
            except ValueError:
                pass
        # 8. Return if the movie is not found
        return None

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

    def update_graph(self):
        movie_name = self.entry_movie.get()
        movie = self.search_movie_bfs(movie_name)

        df2 = pd.read_csv('users.csv', usecols=['Name', 'MovieFavorite'])
        
        df2['MovieFavorite'] = df2['MovieFavorite'].fillna('')

        persons_seen_movie = df2[df2['MovieFavorite'].str.contains(movie_name, case=False)]['Name'].tolist()
        
        self.table_users.delete(*self.table_users.get_children())

        if not persons_seen_movie:
            self.table_users.insert("", "end", values=("No users found.",)) 
        
        for person in persons_seen_movie:
            self.table_users.insert("", "end", values=(person,))
        
        # GETTING DATA:
        # Convert the DataFrame to an N x N matrix
        n = len(self.matrix)  # Number n (adjust as needed)
        node_labels = list(range(n))  # Fill the array with numbers from 0 to n-1

        subgraph = self.matrix
        sub_list = node_labels
        starting_node = None
        if movie is not None:
            starting_node = movie['id']
            reachable_nodes = get_reachable_nodes(self.matrix, node_labels, starting_node)

            subgraph, sub_list = get_subgraph(self.matrix, reachable_nodes, starting_node)
            subgraph = np.array(subgraph)

        sub_list = self.apply_constraint(self.combo_directors.get(), self.combo_genres.get(), sub_list)
        subgraph, sub_list = get_subgraph(self.matrix, sub_list, starting_node)
        if len(sub_list) == 0:
            messagebox.showinfo("ERROR", "No movies meet the filtering criteria...")
            return

        subgraph = np.array(subgraph)
        print(subgraph, sub_list)

        # Create a graph from the adjacency matrix
        G = nx.from_numpy_array(subgraph)
        node_colors = cm.rainbow(np.linspace(0, 1, len(sub_list)))
        color_map = {node: color for node, color in zip(sub_list, node_colors)}

        # Create the graph using networkx and matplotlib
        fig, ax = plt.subplots(figsize=(4, 4))
        nx.draw(G, with_labels=True, ax=ax, labels=dict(zip(G.nodes, sub_list)), node_color=node_colors)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        
        # Create the FigureCanvasTkAgg widget with a fixed size
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().configure(width=400, height=450)
        canvas.draw()
        canvas.get_tk_widget().place(x=645, y=100)

        # Create the matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.place(x=645, y=510)

        self.update_table(sub_list)

if __name__ == "__main__":
    # This block will only be executed if the script is run directly, not if it is imported as a module
    main_window = MainWindow()
    main_window.mainloop()