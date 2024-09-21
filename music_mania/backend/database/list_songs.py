from db_setup import db

def list_songs():
    songs = db['songs'].find()
    for song in songs:
        print(song)

if __name__ == "__main__":
    list_songs()
