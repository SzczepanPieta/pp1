class Music():
    
    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year

    
    
    def __str__(self):
        return f"Performer: {self.performer}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

song1=Music("Ed Sheeran", "Hearts Don't Break Around Here","Divide",2017)
song2=Music("Ed Sheeran", "Hearts Don't Break Around Here","Divide",2017)
song3=Music("Ed Sheeran", "Hearts Don't Break Around Here","Divide",2017)
        
        
print(song1,song2,song3)
