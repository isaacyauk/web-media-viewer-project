from googleapiclient.discovery import build
import os

def get_channel_id_from_url(url):
    # TODO: Parse URL to extract channel ID
    # Handle: /channel/UCxxxx, /@handle, /c/custom, /user/username
    # Use regex or string parsing
    # May need API call for @handles
    pass

def get_recent_videos(channel_id):
    # TODO: Call YouTube API search endpoint
    # Return list of video dicts (video_id, title, published_at, etc)
    pass