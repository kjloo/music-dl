from typing import List
import yt_dlp
from models.song import Song, SongCSV
from models.album import Album


def download_audio(songs: List[Song]):
    base_url = "https://www.youtube.com/watch?v="
    url_list = [f"{base_url}{song.music}" for song in songs]
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list)


if __name__ == "__main__":
    input_file: str = 'input/source.csv'  # Update with the name of your CSV file
    output_dir: str = 'output'

    songs: List[Song] = SongCSV(input_file).read_csv()
    # download_audio(songs)

    album: Album = Album(output_dir)
    album.download_images(songs)
