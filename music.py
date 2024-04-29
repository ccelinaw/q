class Music:
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

#setter for streams
