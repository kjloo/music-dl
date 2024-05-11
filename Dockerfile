# Start from the latest Ubuntu image
FROM ubuntu:latest

# Update packages and install necessary dependencies
RUN apt update && \
    apt install -y python3-pip && \
    apt clean

# # Clean
# RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED

# # Install python package
# RUN pip install -r input/requirements.txt

# Set the working directory
WORKDIR /usr/src/app

# Copy scripts
COPY music_dl.py .

# Set the entry point to run yt-dlp when the container starts
ENTRYPOINT ["python", "music_dl.py"]
