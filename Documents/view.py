import sqlite3
from datamodel.movie import Movie

class View:

    def __init__(self, name):
        self.name = name

    def movies(self):
        movies = []
        # Spajanje na bazu podataka
        conn = sqlite3.connect(self.name)
        # Kreiranje kursora
        cursor = conn.cursor()
        # Izvršavanje upita za dohvat svih filmova
        cursor.execute("SELECT title, year FROM movies")
        # Prolazak kroz sve dohvaćene zapise i stvaranje objekata klase Movie
        for movie_data in cursor.fetchall():
            movies.append(Movie(*movie_data))
        # Zatvaranje veze s bazom
        conn.close()
        return movies
