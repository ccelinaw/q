from music import Music

class Song(Music):
  '''
  A song object that has the artist's name, track name, number of streams and the year the song was released.

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
  add_streams -> string
    Updates the song's streams depending on how many times the user streamed it
  average_danceability -> string
    Returns the average danceability of a song, depending on the user's inputted danceability and the dataset's danceability value

  '''
  def __init__(self, artist_name, streams, track_name, danceability, energy, liveness, year_released):
    '''
    Constructor to build a song object

    Parameters
    ----------

    '''
    super().__init__(artist_name, track_name, streams, danceability, energy, liveness)
    self.__year_released = year_released

  # Method to get the year released of a song
  def get_year_released(self):
    return self.__year_released

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

  def average_danceability(self, new_danceability):
    '''
    Updates the danceability of a song based on the user's tendency to dance to it. The user's input will be averaged with the dataset's danceability value to achieve the new danceability value.

    Parameters
    ----------
    new_danceability
      The danceability ranking that the user has given the song.

    Returns
    -------
    string
      Returns a string that states the track name, artist's name and the new danceability value
    '''
    self.__danceability = (self.__danceability + new_danceability) / 2
    return f'Updated danceability for "{self.__track_name}" by {self.__artist_name}: {self.__danceability}'
