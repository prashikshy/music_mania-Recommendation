from pymongo import MongoClient

# Replace <password> with your MongoDB Atlas password
client = MongoClient('mongodb+srv://prashiksha:me123456789@music-maina.gbuhf.mongodb.net/')
db = client['music_library']  # Database name
collection = db['songs']  # Collection name

# Define the song data
song = {
  "title": "Raaji Bhaye",
  "artist": "Mina Lama, Milan Lama",
  "album": "CRBT Collection",
  "duration": "3:40",
  "file_path": "C:/Users/user/Desktop/Projects/songs/raaji_bhaye.mp3"
}

# Insert the song data into MongoDB
collection.insert_one(song)

print("Song inserted successfully!")
