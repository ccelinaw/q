class Song:
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
  def __init__(self, artist_name, streams, track_name, danceability, energy, liveness):
    '''
    Constructor to build a book object

    Parameters
    ----------
    author: str
      The name of the author of the book
    price: float, optional
      The initial price of the book
      The default price of a book is 0.00 if none is entered
    title: str
      The title of the book
    '''
    self.__artist_name = artist_name
    self.__streams = streams
    self.__track_name = track_name
    self.__danceability = danceability
    self.__energy = energy
    self.__liveness = liveness

  def get_artist_name(self):
    '''
    Returns the artist's name

    Returns
    -------
    The artist's name
    '''
    return self.__artist_name

  def get_streams(self): 
    '''
    Returns the number of streams

    Returns
    -------
    The number of streams
    '''
    return self.__streams

  def get_track_name(self):
    '''
    Returns the track's name

    Returns
    -------
    The track's name
    '''
    return self.__track_name

  def get_danceability(self):
    '''
    Returns the danceability of a song

    Returns
    -------
    The danceability of a song
    '''
    return self.__danceability

  def get_energy(self):
    '''
    Returns the energy level of a song

    Returns
    -------
    The energy level of a song
    '''
    return self.__energy

  def get_liveness(self):
    '''
    Returns the liveness of a song

    Returns
    -------
    The liveness of a song
    '''
    return self.__liveness

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
