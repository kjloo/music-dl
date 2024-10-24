import os

export_video = os.getenv('EXPORT_VIDEO', "false").lower() == "true"
