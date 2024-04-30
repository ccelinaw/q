class Music:
  '''
  A parent music object that has the artist's name, a list of their songs, and their metrics (danceability, energy, liveness)

Attributes
----------
artist_name: string
  The name of the artist of the song.
streams: integer
  The amount of streams the song has.
track_name: string
  The name of the song.
danceability: integer
  How danceable a song is (the user's tendency to dance to this song)
energy: integer
  The energy level of a song (high, low)
liveness = integer
  The presence of live performance elements (audience, cheering)

Methods
-------
get_artist_name -> string
  Returns the name of the artist
get_streams -> integer
  Returns the number of streams a song has
get_track_name -> string
  Returns the track name of the song
get_danceability -> integer
  Returns the danceability of a song
get_energy -> integer
  Returns the energy level of a song
get_liveness -> integer
  Returns the liveness of a song
set_streams -> None
  Sets the number of streams a song has
set_track_name -> None
  Sets the track name of the song
set_artist_name -> None
  Sets the name of the artist
set_danceability -> None
  Sets the danceability of a song
add_streams -> string
  Updates the song's streams depending on how many times the user streamed it
'''
  def __init__(self, artist_name, track_name, streams, danceability, energy, liveness):
    self.__artist_name = artist_name
    self.__track_name = track_name
    self.__streams = streams
    self.__danceability = danceability
    self.__energy = energy
    self.__liveness = liveness

  def get_artist_name(self):
    return self.__artist_name

  def get_track_name(self):
    return self.__track_name

  def get_streams(self):
    return self.__streams

  def get_danceability(self):
    return self.__danceability

  def get_energy(self):
    return self.__energy

  def get_liveness(self):
    return self.__liveness

  def set_streams(self, streams):
    self.__streams = streams

  def set_track_name(self, track_name):
    self.__track_name = track_name

  def set_artist_name(self, artist_name):
    self.__artist_name = artist_name

  def set_danceability(self, danceability):
    self.__danceability = danceability

  # Method to update streams based on a multiplier factor
  def add_streams(self, additional_streams):
    '''
    Updates the stream count of a song after the user has listened to it

    Parameters
    ----------
    additional_streams
      The value to increase the number of streams by

    Returns
    -------
    string
      Returns a string that states the song's name, the artist's name and the new number of streams
    '''
    self.__streams += additional_streams
    return f'Updated stream count for "{self.__track_name}" by {self.__artist_name}: {self.__streams}'
