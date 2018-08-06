import wikipedia
import clr


clr.AddReference("System.Net")
from System.Net import WebClient

clr.AddReference("System.IO")
from System.IO import MemoryStream

MemoryStream(WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg'))

def do_fetch(source, **kwargs):
	if kwargs["title"]:
		print kwargs["title"]
		wikisource()
		# source.findByName(kwargs["title"])
	else:
		print "no title"

class wikisource:

	def __init__(self):
		a = wikipedia.suggest("Roundabout")