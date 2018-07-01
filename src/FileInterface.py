import sys
sys.path.append(r'C:\Python27\Lib')

import clr
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import File

f = File.Create(r'../test/Blackened.mp3')

class FileInterface:

    def __init__(self, path=""):
        self.file = File.Create(path)

    def GetTitle(self):
        return self.file.Tag.Title

    def GetAlbum(self):
        return self.file.Tag.Album

    def GetPicture(self):
        return self.file.Tag.Pictures[0].Data

    def GetMainArtist(self):
        return self.file.Tag.AlbumArtists[0]

    def GetPerformers(self):
        return self.file.Tag.Performers

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

