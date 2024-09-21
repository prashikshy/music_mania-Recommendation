from db_setup import db
from pymongo import MongoClient
import pandas as pd

def get_songs():
    """Retrieve all songs from the database."""
    songs = list(db['songs'].find())
    print(songs)  # Add this line to check the output
    return pd.DataFrame(songs)

def recommend_songs(selected_song_title, num_recommendations=5):
    """Recommend songs based on the selected song's features."""
    songs_df = get_songs()

    # Get the features of the selected song
    selected_song = songs_df[songs_df['title'] == selected_song_title].iloc[0]

    # Calculate similarity based on genre, tags, or artist
    # You can modify this to include more features or use a different method
    similar_songs = songs_df[
        (songs_df['genre'] == selected_song['genre']) |
        (songs_df['artist'].apply(lambda x: any(artist in x for artist in selected_song['artist'])))
    ]

    # Exclude the selected song from the recommendations
    similar_songs = similar_songs[similar_songs['_id'] != selected_song['_id']]

    # Return the top N recommendations
    return similar_songs.head(num_recommendations)

def main():
    songs_df = get_songs()
    print("Available songs:")
    print(songs_df['title'].tolist())  # Print all song titles

    selected_song_title = input("Enter the title of the song for recommendations: ")
    recommendations = recommend_songs(selected_song_title)

    if recommendations.empty:
        print("No recommendations found.")
    else:
        print("Recommended songs:")
        for index, song in recommendations.iterrows():
            print(f"Title: {song['title']}, Artists: {', '.join(song['artist'])}, Genre: {song['genre']}")

if __name__ == "__main__":
    main()
