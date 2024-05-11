from typing import List
from models.song import Song
import re
import urllib.request
import os.path

SPOTIFY_BASE = 'https://open.spotify.com/album/'


class Album:
    def __init__(self, dst_dir: str):
        self.dst_dir = dst_dir

    def _download_image(self, album: str):
        full_link = SPOTIFY_BASE + album

        response = urllib.request.urlopen(full_link)
        html_text = response.read().decode('utf-8')

        m = re.compile(r'"(https://i\.scdn\.co\/image\/\w+)"')
        s = m.search(html_text)
        image_url = s.group(1)
        urllib.request.urlretrieve(
            image_url, os.path.join(self.dst_dir, album + '.jpg'))

    def download_images(self, songs: List[Song]):
        albums = list(set([song.album for song in songs]))
        for album in albums:
            self._download_image(album)
