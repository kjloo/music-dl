# Start from the latest Ubuntu image
FROM ubuntu:latest

# Update packages and install necessary dependencies
RUN apt update && \
    apt install -y python3-pip && \
    apt install -y ffmpeg && \
    apt clean

# # Clean
RUN rm /usr/lib/python3.12/EXTERNALLY-MANAGED

# # Install python package
RUN pip3 install yt-dlp

# # Copy scripts
COPY app /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Set the entry point to run yt-dlp when the container starts
ENTRYPOINT ["python3", "music_dl.py"]
# ENTRYPOINT ["/bin/bash"]
