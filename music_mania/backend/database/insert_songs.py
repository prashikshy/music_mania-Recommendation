import os
from db_setup import db
from pymongo.errors import DuplicateKeyError

def clear_songs():
    """Clear all existing songs from the database."""
    db['songs'].delete_many({})
    print("All songs cleared from the database.")

def insert_song(song):
    """Inserts a single song into the songs collection."""
    try:
        result = db['songs'].insert_one(song)
        print(f"Inserted song with _id: {result.inserted_id}")
    except DuplicateKeyError:
        print(f"Song with _id: {song['_id']} already exists.")

def main():
    clear_songs()

    # Directory containing your songs
    songs_directory = "C:/Users/user/Desktop/Projects/songs"

    # Loop through files in the directory and create song metadata
    songs = []
    for filename in os.listdir(songs_directory):
        if filename.endswith(".mp3"):
            song_id = f"song_{len(songs) + 1:03}"  # Generate unique song ID
            song = {
                "_id": song_id,
                "title": os.path.splitext(filename)[0],  # Use the file name as title
                "artist": ["Unknown Artist"],  # Modify this as needed
                "album": "Unknown Album",  # Modify this as needed
                "genre": "Unknown Genre",  # Modify this as needed
                "tags": ["unknown"],  # Modify this as needed
                "duration": "0:00",  # Update this if you can extract duration
                "file_path": os.path.join(songs_directory, filename)
            }
            songs.append(song)

    for song in songs:
        insert_song(song)

if __name__ == "__main__":
    main()
