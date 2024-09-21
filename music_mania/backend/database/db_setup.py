# db_setup.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

# Set up MongoDB connection
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Example function to create 'songs' collection
def create_songs_collection():
    collection = db['songs']  # This will create the collection if it doesn't exist
    return collection

# Example function to insert a song document into the collection
def insert_song(song_data):
    songs_collection = create_songs_collection()
    songs_collection.insert_one(song_data)

# Sample usage
if __name__ == "__main__":
    sample_song = {
        "title": "Song Title",
        "artist": "Artist Name",
        "album": "Album Name",
        "genre": "Genre",
        "year": 2024,
        "duration": 215,  # Duration in seconds
        "path": "/path/to/song/file"
    }
    insert_song(sample_song)
    print("Sample song inserted into MongoDB!")
