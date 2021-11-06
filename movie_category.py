import csv
from movie import Movie


class MovieCategory:

    def __init__(self):
        self.filename = 'movies.csv'
        self.all_movie = self.define_movie()

    def define_movie(self):
        rows = []
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                rows.append(row)
        return rows

    def get_movie(self, title):
        for i in range(self.all_movie[0]):
            if self.all_movie[0][i][1] == title:
                return Movie(self.all_movie[0][i][1],
                             self.all_movie[0][i][2], self.all_movie[0][i][3])
