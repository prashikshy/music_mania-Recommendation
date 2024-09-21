# models.py

from .db_setup.py import db

# Collections
users_collection = db['users']
songs_collection = db['songs']

# Example of a user document structure
user_document = {
    "_id": "user_123",  # Unique identifier
    "username": "JohnDoe",
    "preferences": ["pop", "rock"]  # Genres the user likes
}

# Example of a song document structure
song_document = {
    "_id": "song_001",  # Unique identifier
    "title": "Raaji Bhaye",
    "artist": ["Mina Lama", "Milan Lama"],
    "album": "CRBT Collection",
    "genre": "pop",
    "tags": ["nepali", "pop", "modern"],
    "duration": "3:40",
    "file_path": "C:/Users/user/Desktop/Projects/songs/raaji_bhaye.mp3"
}
