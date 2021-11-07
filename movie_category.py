import csv
from movie import Movie


class MovieCategory:

    def __init__(self):
        self.filename = 'movies.csv'
        self.all_movie = []

    def get_movie(self, title):
        if len(self.all_movie) == 0:
            with open(self.filename, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[1] == title:
                        self.all_movie.append(Movie(row[1], row[2], row[3].split('|')))
                        return Movie(row[1], row[2], row[3].split('|'))
                    self.all_movie.append(Movie(row[1], row[2], row[3].split('|')))

        for i in range(len(self.all_movie)):
            if self.all_movie[i].get_title() == title:
                return self.all_movie[i]

        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            for i in range(len(self.all_movie), len(csvreader)):
                if csvreader[i] == title:
                    self.all_movie.append(Movie(csvreader[i][1], csvreader[i][2], csvreader[i][3].split('|')))
                    return Movie(csvreader[i][1], csvreader[i][2], csvreader[i][3].split('|'))
                self.all_movie.append(Movie(csvreader[i][1], csvreader[i][2], csvreader[i][3].split('|')))
