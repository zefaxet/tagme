from sys import argv
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC, TRCK

tags = ID3("C:\\Users\\Edward Auttonberry\\Desktop\\music\\" + input() + ".mp3")

for x in argv:
    if x in arglist:
        argdict[x] = argv[argv.index(x) + 1]

for x in argdict.keys():
    arg = argdict[x]
    if x == "-filename":
        pass
    if x == "-title":
        tags["TIT2"] = TIT2(encoding=3, text=arg)
    if x == "-aartist":
        tags["TPE2"] = TPE2(encoding=3, text=arg)
    if x == "-album:":
        tags["TALB"] = TALB(encoding=3, text=arg)  # Album name
    if x == "-tracknum":
        tags["TRCK"] = TRCK(encoding=3, text=arg)
    if x == "-year":
        tags["TDRC"] = TDRC(encoding=3, text=arg)
    if x == "-genre":
        tags["TCON"] = TCON(encoding=3, text=arg)
    if x == "-test": #doesnt work
        tags["TCOM"] = TCOM(encoding=3, text=arg)

tags.save("C:\\Users\\Edward Auttonberry\\Desktop\\Blackened.mp3")

#TALB Album
#TBPM bpm
#TCOM composer
#TCON Content type (Genre) -- Use genres instead of text attribute
#TCOP copyright(c)
#TCMP itunes compilation flag
#TDAT date of recording (ddmm)
#TDEN encoding time
#TEXT lyricist
#TFLT file type
#TIME time of recording (HHMM)
#TIT2 Title
#TIT3 Subtitle
#TKEY starting key
#TLEN starting length
#TMOO mood
#TOAL original Album
#TOFN original filename
#TOLY original lyricist
#TOPE original artist/performer
#TORY original release year
#TOWN owner/licensee
#TPE1 Lead Artist/Performer/Soloist/Group
#TPE2 Band/Orchestra/Accompaniment
#TPE3 Conductor
#TPE4 Interpreter/Remixer/Modifier
#TPRO Produced
#TPUB Publisher
#TRCK Track Number
#TRDA Recording Dates
#TSIZ Size of Audio Data (bytes)
#TYER Year of Recording
#TXXX User-Defined text data
#WXXX User-Defined url data
#IPL Involved people
#USLT Lyrics (unsynchronized) lang(CHAR 3), desc(FREEFORM), text(FREEFORM)
#SYLT Synced Lyrics
#COMM User comment
#APIC Image data -- encoding for desc, mime for image type (MIME for image/jpeg or --> for URI), type is source (3 is front cover), desc is description of image, data is image data (bytestring)
#PCNT play counter
#POPM rating and play count to email -- email: email associated, rating: 0 - 255, count: number of plays (opt)
