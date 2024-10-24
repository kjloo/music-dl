import csv
import yt_dlp

YOUTUBE_BASE = 'https://www.youtube.com/watch?v='


class Song:
    def __init__(self, title: str, music: str, album: str, image: str, download_video: bool):
        self.title = title
        self.music = music
        self.album = album
        self.image = image
        self.download_video = download_video
        if self.download_video:
            self.options = {
                'outtmpl': f'output/{self.album}/{self.title}',
                'format': 'bestvideo+bestaudio',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
            }
        else:
            self.options = {
                'outtmpl': f'output/{self.album}/{self.title}.mp3',
                'format': 'bestaudio/best',
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
                            row['Album'], row['Image'], row['Video'].lower() == "true")
                songs.append(song)
        return songs
