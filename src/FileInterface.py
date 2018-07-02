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

    def get_album(self):
        return self.file.Tag.Album

    def get_picture(self):
        return self.file.Tag.Pictures[0].Data

    def get_main_artist(self):
        return self.file.Tag.AlbumArtists[0]

    def get_performers(self):
        return self.file.Tag.Performers

    def get_genre(self):
        return self.file.Tag.Genre

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

