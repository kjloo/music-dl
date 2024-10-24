# Music Downloader

A wrapped container for downloading music.

## Instructions

1. Build the docker `docker build -t music-dl .`
2. `cp input/source.csv.example input/source.csv`
3. `cp .env.example .env`
4. Run the image `docker-compose up` or `docker-compose exec music-dl /bin/bash`

### Configuration

In the `.env` file

| Variable     | Use                        | Default |
| ------------ | -------------------------- | ------- |
| EXPORT_VIDEO | Download the video as well | False   |
