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


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.tk_setPalette(background='#2E2E2E', foreground='white')
        label_font = ('Montserrat', 10)
        self.title("Movie Suggestions")
        self.geometry("1280x600")

         # Crear un tema de estilo
        style = ttk.Style(self)
        
        # Configurar el tema para el Combobox
        style.theme_create("custom_theme", parent="alt", settings={
            "TCombobox": {
                "configure": {"selectbackground": 'white', "fieldbackground": '#2E2E2E', "foreground": 'white'},
            }
        })

        style.theme_use("custom_theme")

        self.label_movie = tk.Label(self, text="Enter the name of the movie:", fg='white', bg = 'black', font=label_font)
        self.label_movie.place(x=20, y=45)

        self.entry_movie = tk.Entry(self)
        self.entry_movie.place(x=250, y=45)

        self.button_update = tk.Button(self, text="Search person", command=self.make_suggestion, fg='white', bg = 'blue', font=label_font)
        self.button_update.place(x=450, y=40)

        # Create a table
        self.table = ttk.Treeview(self, columns=("Name"), show="headings", style="mystyle.Treeview")
        self.table.column("Name", width=150)
        self.table.heading("Name", text="Name")

        # Create a scrollbar and associate it with the table
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)

        # Position the table and scrollbar in the window
        self.table.place(x=430, y=100, width=600, height=450)
        scrollbar.place(x=1030, y=100, height=450)

        # Read the CSV file and store it in a DataFrame
        df = pd.read_csv('users.csv', usecols=['MovieFavorite'])

        # Create an example graph
        self.update_graph()

    def make_suggestion(self):
         # Obtén el nombre de la película ingresado por el usuario
         movie_name = self.entry_movie.get().strip()
        
         # Lee el archivo CSV y obtén los nombres de los usuarios que tienen la película como favorita
         df = pd.read_csv('users.csv', usecols=['Name', 'MovieFavorite'])
        
         # Maneja el caso de NaN en la columna 'MovieFavorite'
         df['MovieFavorite'] = df['MovieFavorite'].fillna('')
        
         # Filtra el DataFrame para obtener usuarios con la misma película
         persons_seen_movie = df[df['MovieFavorite'].str.contains(movie_name, case=False)]['Name'].tolist()
        
         # Limpia la tabla antes de agregar nuevos resultados
         self.table.delete(*self.table.get_children())
        
         # Agrega los nombres de los usuarios a la tabla
         for person in persons_seen_movie:
             self.table.insert("", "end", values=(person,))
        

    def update_graph(self):
        pass

if __name__ == "__main__":
    # This block will only be executed if the script is run directly, not if it is imported as a module
    main_window = MainWindow()
    main_window.mainloop()