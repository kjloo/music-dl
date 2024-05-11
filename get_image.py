import re
import urllib

SPOTIFY_BASE = 'https://open.spotify.com/album/'
DEST_DIR = '/home/kaleb/Downloads/'
with open(DEST_DIR + 'tag.txt', 'r') as f:
    tag = f.read()

full_link = SPOTIFY_BASE + tag

response = urllib.urlopen(full_link)
html_text = response.read()

m = re.compile(r'"(https://i\.scdn\.co\/image\/\w+)"')
s = m.search(html_text)
image_url = s.group(1)
urllib.urlretrieve(image_url, DEST_DIR + 'cover.jpg')
