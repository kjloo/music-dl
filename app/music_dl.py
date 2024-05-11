from typing import List
from models.song import Song, SongCSV
from models.album import Album


def download_audio(songs: List[Song]):
    for song in songs:
        song.download()


if __name__ == "__main__":
    input_file: str = 'input/source.csv'  # Update with the name of your CSV file
    output_dir: str = 'output'

    songs: List[Song] = SongCSV(input_file).read_csv()
    download_audio(songs)

    album: Album = Album(output_dir)
    album.download_images(songs)
