class Song:
    pass
    #define our class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self,name,artist,genre):
        pass
        #instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        #other attributes
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre,1)
        self.add_to_artist_count(self.artist,1)
        
    #class methods
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
        
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            pass
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            pass
    
    @classmethod
    def add_to_genre_count(cls, genre, songs):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = songs
        else:
            cls.genre_count[genre] += songs
            
    @classmethod
    def add_to_artist_count(cls, artist, songs):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = songs
        else:
            cls.artist_count[artist] += songs
        
        