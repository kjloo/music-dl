import csv
import yt_dlp

YOUTUBE_BASE = 'https://www.youtube.com/watch?v='


class Song:
    def __init__(self, title, music, album, image):
        self.title = title
        self.music = music
        self.album = album
        self.image = image
        self.options = {
            'outtmpl': f'output/{self.album}/{self.title}',
            'format': 'bestaudio/best',
            'audioformat': 'mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    def download(self):
        url = f"{YOUTUBE_BASE}{self.music}"

        with yt_dlp.YoutubeDL(self.options) as ydl:
            ydl.download(url)


class SongCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        songs = []
        with open(self.csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                song = Song(row['Song'], row['Music'],
                            row['Album'], row['Image'])
                songs.append(song)
        return songs
