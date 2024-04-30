from music import Music

class Artist(Music):
  '''
  An artist object that has a list of an artist's songs and the total values of their metrics (danceability, energy, liveness)

  Attributes
  ----------
  songs: list of song objects
    The songs that belong to the artists
  total_danceability: integer
    The total danceability of the artist's songs (to be averaged)
  total_energy: integer
    The total energy of the artist's songs (to be averaged)
  total_liveness: integer
    The total liveness of the artist's songs (to be averaged)
  total_streams: integer
    The total number of streams the artist has

  Methods
  -------
  add_songs -> None
    Adds a song to the artist's list of songs and its metrics
  get_average_metrics -> dictionary
    The average danceability, energy and liveness of an artist's song
  recommend_song -> song object
    Recommends the user a song based on their preferences
  add_streams -> None
    Updates the number of streams the artist has
  update_metrics -> None
    Updates each of the metrics (danceability, energy, liveness)
  '''
  
  def __init__(self, artist_name):
    '''
    Constructor to build an artist object

    Parameters
    ----------
    artist_name: the artist's name
    '''
    super().__init__(artist_name, '', 0, 0, 0, 0)
    self.__songs = []
    self.__total_danceability = 0
    self.__total_energy = 0
    self.__total_liveness = 0
    self.__total_streams = 0

  def get_songs(self):
    '''
    Returns the songs that belong to the artist

    Returns
    -------
    The artist's song catalogue
    '''
    return self.__songs

  def add_song(self, song):
    '''
    Adds a song to the artist's list of songs.

    Parameters
    ----------
    song: string
      The track name of the song that is to be added to the artist's list of songs
    '''
    self.__songs.append(song)
    self.__total_danceability += song.get_danceability()
    self.__total_energy += song.get_energy()
    self.__total_liveness += song.get_liveness()

  def get_average_metrics(self):
    '''
    Returns the average danceability, energy and liveness of the artist's songs (considered the song's "metrics")

    Returns
    -------
    integer
      Returns the integer values of the average danceability, energy and liveness of the artist's songs

    Raises
    ------
    AttributeError
      If the attribute is non-existent and Python cannot add to it
    '''
    total_songs = len(self.__songs)
    if total_songs == 0:
      return AttributeError('No songs have been added to the artist yet.')
    metrics = {
      'Average Danceability ': int(self.__total_danceability // total_songs),
      'Average Energy ': int(self.__total_energy // total_songs),
      'Average Liveness ': int(self.__total_liveness // total_songs)
    }
    return metrics

  def recommend_song(self):
    '''
    Recommends the user a song based on the user's input

    Returns
    -------
    string
      Returns the recommended song which is the song with the highest stream count from that artist

    Raises
    ------
    AttributeError
      If the attribute is non-existent and Python cannot access it (the artist has no songs)
    '''
    if not self.__songs:
      return AttributeError
    max_streams = 0
    for song in self.__songs:
      if song.get_streams() > max_streams:
        max_streams = song.get_streams()
        recommended_song = song
    return recommended_song

def add_streams(self, additional_streams):
  '''
  Updates the stream count of the artist based on the user's input

  Parameters
  ----------
  additional_streams
    The value to increase the number of streams by

  Returns
  -------
  string
    Returns a string that states the updated stream count for the artist
  '''
  for song in self.__songs:
    song.add_streams(additional_streams)
  self.__total_streams += additional_streams
  return f'Updated stream count: "{self.__total_streams}"'

def __update_metrics(self, song):
  '''
  Updates the artist's metrics (danceability, energy, liveness) when a new song is added
  
  Returns
  -------
  integer
    Updates each of the metrics
  '''
  self.__total_danceability += song.get_danceability()
  self.__total_energy += song.get_energy()
  self.__total_liveness += song.get_liveness()
