import sys
sys.path.append(r'C:\Python27\Lib')

import clr
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import File

f = File.Create(r'../test/Blackened.mp3')
print f.Tag.Album
