import csv
import random
from artist import Artist
from song import Song
from simplify import simplify
'''import pyrebase

firebase_config =   {
  "apiKey": "AIzaSyB6VUKfCQZa8N3oINxTcAsbT8KqMKfW1HA",
  "authDomain": "database-cf351.firebaseapp.com",
  "databaseURL": "https://database-cf351-default-rtdb.firebaseio.com/",
  "projectId": "database-cf351",
  "storageBucket": "database-cf351.appspot.com",
  "messagingSenderId": "213042461007",
  "appId": "1:213042461007:web:d0bc5ae4d4126bac4f2d3a",
  "measurementId": "G-KF4H10EKCJ"
  }'''
#---------------------------------------------------------------------------
# Name:        Individualized Long-Term Project
# Purpose:     Finding Trends in the Top Spotify Songs of 2023.
#              				
#
# Author:      Celina Wang
# Created:     20-Feb-2024
# Updated:     
#---------------------------------------------------------------------------

# List that corresponds the numerical month value with a string value for readability in comparisons.
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

artists = {}
songs = []
main_song_info = []
# Reads the dataset, applies variables to each row index and converts values if necessary.
with open('dataset.csv') as user_dataset:
  csv_reader = csv.reader(user_dataset, delimiter=',')
  for row in csv_reader:
    # Checks if the row has all the necessary values.
    if len(row) == 19:
      try:
        track_name = row[0]
        artist_names = row[1].split(', ')
        year_released = int(row[3])
        streams = int(row[7])
        danceability = float(row[12])
        energy = float(row[14])
        liveness = int(row[17])

        # Creates a Song object for all the artists involved
        song = Song(artist_names, streams, track_name, danceability, energy, liveness, year_released)
        songs.append(song)
        for artist_name in artist_names:
          artist_name = artist_name.strip()
          if artist_name not in artists:
            artists[artist_name] = Artist(artist_name)
          artists[artist_name].add_song(song)

        artist_count = int(row[2])
        month_released = months[int(row[4])]
        day_released = int(row[5])
        spotify_playlists = simplify(int(row[6]))
        
        # Streams, track name and artist name are added to a list (to be written in local csv file and firebase.
        main_song_info.append([streams, track_name, artist_name])
        
        apple_playlists = int(row[8])
        bpm = int(row[9])
        key = row[11]
        mode = row[12]
        valence = int(row[13])
        acousticness = int(row[15])
        instrumentalness = int(row[16])
        speechiness = int(row[18])
      # If any row does not have all the information, skips that row's values
      except ValueError:
        continue

# Shuffles the list of artist names for different recommendations and provides the artist's songs and details (metrics)
artist_names = list(artists.keys())
random.shuffle(artist_names)
for artist_name in artist_names:
  artist = artists[artist_name]
  if len(artist.get_songs()) >= 3:
    print(f"Artist: {artist_name}")
    print("Songs:")
    for song in artist.get_songs():
      print(f" - {song.get_track_name()}")
    print("Artist Details: ")
    for metric, value in artist.get_average_metrics().items():
      print(f"{metric}: {value}")

  # Asks the user if they enjoy listening to this artist, if an invalid answer is entered, will recommend a different artist
    user_input = input('\nDo you like this artist (yes/no/stop): ').strip().lower()
    if user_input == 'yes':
    # Recommends another song from this artist with the song's details
      recommended_song = artist.recommend_song()
      if recommended_song:
        print(f"\nWe recommend you listen to '{recommended_song.get_track_name()}")
        print(f"Details: Danceability: {recommended_song.get_danceability()}, Energy: {recommended_song.get_energy()}, Liveness: {recommended_song.get_liveness()}")

      # Updates the song's streams and averages danceability rating depending on the user's input
      stream_count = int(input("How many times did you listen to the recommended song?: ").strip())
      danceability_rating = int(input("On a scale of 1-100, how danceable do you think the song is?: ").strip())
      while not 1 <= float(danceability_rating) <= 100:
        danceability_rating_input = int(input("Please enter a valid response (1-100):").strip())
      recommended_song.add_streams(stream_count)
      recommended_song.average_danceability(danceability_rating)
      print(f"The updated stream count for {recommended_song.get_track_name()} is now {recommended_song.get_streams()} streams.")
      print(f"The updated average danceability rating is now {recommended_song.get_danceability()}.")

      # If the user enjoyed the song that was recommended, another song gets recommended
      user_opinion = input("Did you like this song? (yes/no): ").strip().lower()
      if user_opinion == 'yes':
        other_artists_songs = [song for song in artist.get_songs() if song.get_track_name() != recommended_song.get_track_name()]
        if other_artists_songs:
          second_recommendation = random.choice(other_artists_songs)
          print(f"Since you liked {recommended_song.get_track_name()}, you might also like {second_recommendation.get_track_name()}")
          break
      else:
        print("This artist has no available songs to be recommended")

# If the user said stop or any other response, the program will stop
    elif user_input == 'stop':
      print("Stopping the recommendation process.")
      break
    if not user_input == 'yes':
      print("\nNo more artists to suggest.")

# Writes the top 100 most streamed songs onto a local CSV file, as well as a Firebase (external database) which allows the data to be organized and adaptable.
# data = {'Top Songs': []}
main_song_info.sort(reverse=True)
# Writes to local CSV file
with open('top_streams.csv', 'w') as top_streams:
  top_streams.write('Track Name, Artist Name, Streams\n')
  for i in range(100):
    top_streams.write(str(i+1) + '. ' + (main_song_info[i][1]) + ' by ' + (main_song_info[i][2]) + ' has ' + (simplify(main_song_info[i][0])) + ' streams.\n')

'''# Writes to Firebase external database
    data['Top Songs'].append({
      'Track Name:' : main_song_info[i][1],
      'Artist Name' : main_song_info[i][2],
      'Streams' : main_song_info[i][0]
    })
firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()
database.push(data)'''
