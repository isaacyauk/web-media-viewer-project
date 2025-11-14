from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# TODO: Define User table (id, username, email)
# TODO: Define YouTubeChannel table (id, user_id, channel_id, channel_name)
# TODO: Define YouTubeVideo table (id, video_id, channel_id, title, published_at)
# TODO: Define YouTubeUserVideoStatus table (id, user_id, video_id, seen)