# Start from the latest Ubuntu image
FROM ubuntu:latest

# Update packages and install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean

# Install yt-dlp using pip3
RUN pip3 install yt-dlp

# Set the working directory
WORKDIR /usr/src/app

# Copy scripts
COPY get_image.py .

# Set the entry point to run yt-dlp when the container starts
ENTRYPOINT ["/bin/bash"]
