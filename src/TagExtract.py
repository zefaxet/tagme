import sys
sys.path.append(r'C:\Python27\Lib')

import clr
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import File

f = File.Create(r'../test/Blackened.mp3')

class FileInterface:

    def __init__(self, path):
        self.file = File.Create(path)

    def GetTitle(self):
        return self.file.Title

    def GetPicture(self):
        return self.file.Tag.Pictures[0].Data

print f.Tag.Pictures[0].Data
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

