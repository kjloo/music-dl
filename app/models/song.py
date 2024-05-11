import csv


class Song:
    def __init__(self, title, music, album):
        self.title = title
        self.music = music
        self.album = album


class SongCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        songs = []
        with open(self.csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                song = Song(row['Song'], row['Music'], row['Album'])
                songs.append(song)
        return songs
