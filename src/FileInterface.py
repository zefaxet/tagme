import sys
sys.path.append(r'C:\Python27\Lib')

import clr
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import File

class FileInterface:

    def __init__(self, path=""):
        self.file = File.Create(path)

    def get_title(self):
        return self.file.Tag.Title

    def set_title(self, value):
        self.file.Tag.Title = value

    def get_album(self):
        return self.file.Tag.Album

    def set_album(self, value):
        self.file.Tag.Album = value

    #  TODO figure this cunt out
    def get_picture(self):
        return self.file.Tag.Pictures[0]

    def set_picture(self, data):
        self.file.Tag.Pictures[0].Data = data

    def get_main_artist(self):
        return self.file.Tag.AlbumArtists[0]

    #  TODO setter should accept an Array[str]
    def set_main_artist(self, values):
        self.file.Tag.AlbumArtists[0] = values

    def get_performers(self):
        return self.file.Tag.Performers

    def set_performers(self, values):
        self.file.Tag.Performers = values

    def get_genre(self):
        return self.file.Tag.Genres

    def set_genre(self, values):
        self.file.Tag.Genres = values

    def get_year(self):
        return self.file.Tag.Year

    def set_year(self, value):
        self.file.Tag.Year = value

    def get_track_number(self):
        return self.file.Tag.Track

    def set_track_number(self, value):
        self.file.Tag.Track = value

#  KNOWN FIELDS
#  Name - file path/name

#  KNOWN TAGS
#  Album - album name
#  Comment
#  AlbumArtists - Album Artist (As array of strings, but the field only takes one value)
#  Lyrics
#  Composers
#  Disc - (int)
#  DiscCount
#  Performers - Contributing Artists
#  Title
#  Track
#  TrackCount
#  Year
#  Pictures

