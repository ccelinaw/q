from music import Music

class Song(Music):
  '''
  A song (child) object that inherits attributes and methods from the Music class. Contains all the attributes and methods of a song.

  Attributes
  ----------
  year_released: integer
    The year the song was released.
    
  Methods
  -------
  get_year_released -> integer
    Returns the year the song was released.
  average_danceability -> string
    Returns the average danceability of a song, depending on the user's inputted danceability and the dataset's danceability value

  '''
  def __init__(self, artist_name, streams, track_name, danceability, energy, liveness, year_released):
    '''
    Constructor to build a song object

    Parameters
    ----------
    artist_name
      The name of the song's artist
    streams
      The number of streams the song has
    track_name
      The name of the song
    danceability
      How danceable a song is
    energy
      How energetic the song is
    liveness
      The presence of live performance elements
    year_released
      The year the song was released
    '''
    super().__init__(artist_name, track_name, streams, danceability, energy, liveness)
    self.__year_released = year_released

  # Method to get the year released of a song
  def get_year_released(self):
    return self.__year_released

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
    self._set_danceability = ((self.get_danceability() + new_danceability) / 2)
    return f'Updated danceability for "{self.get_track_name()}" by {self.get_artist_name()}: {self.get_danceability()}'
