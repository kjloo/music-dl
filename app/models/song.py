import csv
import yt_dlp
import subprocess


def convert_vtt_to_srt(base_file: str, languages: list[str]):
    # Construct the FFmpeg command
    for language in languages:
        vtt_file = f"{base_file}.{language}.vtt"
        srt_file = f"{base_file}.{language}.srt"
        command = ['ffmpeg', '-i', vtt_file, srt_file]

        # Run the command
        try:
            subprocess.run(command, check=True)
            print(f"Converted '{vtt_file}' to '{srt_file}' successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")


YOUTUBE_BASE = 'https://www.youtube.com/watch?v='


class Song:
    def __init__(self, title: str, music: str, album: str, image: str, download_video: bool):
        self.title = title
        self.music = music
        self.album = album
        self.image = image
        self.languages = ['ja', 'en']
        self.download_video = download_video
        if self.download_video:
            self.options = {
                'outtmpl': self._create_output(),
                'format': 'bestvideo+bestaudio',
                'subtitleslangs': self.languages,
                'writesubtitles': True,
                'postprocessors': [
                    {
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',
                    },
                    {
                        'already_have_subtitle': True,
                        'key': 'FFmpegEmbedSubtitle'
                    }],
            }
        else:
            self.options = {
                'outtmpl': f'{self._create_output()}.mp3',
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
        if self.download_video:
            convert_vtt_to_srt(self._create_output(), self.languages)

    def _create_output(self) -> str:
        return f'output/{self.album}/{self.title}'


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
