from util.log import create_logger

import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import ComboBox, ComboBoxStyle, PictureBox, PictureBoxSizeMode
clr.AddReference("System.Drawing")
from System.Drawing import Color, Size
clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
from TagLib import PictureType

ID3_TAGS = {
		"Other" : PictureType.Other,
		"File Icon" : PictureType.FileIcon,
		"Other File Icon" : PictureType.OtherFileIcon,
		"Front Cover" : PictureType.FrontCover,
		"Back Cover" : PictureType.BackCover,
		"Leaflet Page" : PictureType.LeafletPage,
		"Media" : PictureType.Media,
		"Lead Artist" : PictureType.LeadArtist,
		"Artist" : PictureType.Artist,
		"Conductor" : PictureType.Conductor,
		"Band" : PictureType.Band,
		"Composer" : PictureType.Composer,
		"Lyricist" : PictureType.Lyricist,
		"Recording Location" : PictureType.RecordingLocation,
		"During Recording" : PictureType.DuringRecording,
		"During Performance" : PictureType.DuringPerformance,
		"Movie Screen Capture" : PictureType.MovieScreenCapture,
		"Fishie" : PictureType.ColoredFish,
		"Illustration" : PictureType.Illustration,
		"Band Logo" : PictureType.BandLogo,
		"Publisher Logo" : PictureType.PublisherLogo,
		"Not a Picture" : PictureType.NotAPicture,
	}

class Selector(ComboBox):

	LOGGER = create_logger("Selector")

	def __init__(self, options, size=None, top=None, left=None):
		ComboBox.__init__(self)
		self.DropDownStyle = ComboBoxStyle.DropDownList
		self.Enabled = False
		if size:
			self.Size = size
		if top:
			self.Top = top
		if left:
		 	self.Left = left
		for frame in options:
			self.Items.Add(frame)
		# 5 is front cover
		self.SelectedItem = self.Items[5]
		self.SelectedValueChanged += self.__selected_value_changed

	def __selected_value_changed(self, sender, args):

		imagetype = ID3_TAGS[self.SelectedItem.ToString()]

class Art(PictureBox):

	def __init__(self, parent):
		self.SizeMode = PictureBoxSizeMode.StretchImage
		self.BackColor = Color.White
		self.Size = Size(160,160)
		self.Top = 50
		self.Left = (parent.Width - self.Width) / 2
		
		parent.Controls.Add(self)
		

		


#the following codeblock sets a placeholder to each of the picture frames on the loaded file
#clr.AddReferenceToFileAndPath(r'../lib/taglib-sharp.dll')
    # from TagLib.Id3v2 import AttachedPictureFrame
    # from TagLib import Picture, PictureType
    # import TagLib.Png as png
    #
    # # x00 = Picture(r'../../0x00.png')
    # # x01 = Picture(r'../../0x01.png')
    # # x02 = Picture(r'../../0x02.png')
    # # x03 = Picture(r'../../0x03.png')
    # # x04 = Picture(r'../../0x04.png')
    # # x05 = Picture(r'../../0x05.png')
    # # x06 = Picture(r'../../0x06.png')
    # # x07 = Picture(r'../../0x07.png')
    # # x08 = Picture(r'../../0x08.png')
    # # x09 = Picture(r'../../0x09.png')
    # # x0A = Picture(r'../../0x0A.png')
    # # x0B = Picture(r'../../0x0B.png')
    # # x0C = Picture(r'../../0x0C.png')
    # # x0D = Picture(r'../../0x0D.png')
    # # x0E = Picture(r'../../0x0E.png')
    # # x0F = Picture(r'../../0x0F.png')
    # # x10 = Picture(r'../../0x10.png')
    # # x11 = Picture(r'../../0x11.png')
    # # x12 = Picture(r'../../0x12.png')
    # # x13 = Picture(r'../../0x13.png')
    # # x14 = Picture(r'../../0x14.png')
    # # xff = Picture(r'../../0xff.png')
    # # x00.Type = PictureType.Other
    # # x01.Type = PictureType.FileIcon
    # # x02.Type = PictureType.OtherFileIcon
    # # x03.Type = PictureType.FrontCover
    # # x04.Type = PictureType.BackCover
    # # x05.Type = PictureType.LeafletPage
    # # x06.Type = PictureType.Media
    # # x07.Type = PictureType.LeadArtist
    # # x08.Type = PictureType.Artist
    # # x09.Type = PictureType.Conductor
    # # x0A.Type = PictureType.Band
    # # x0B.Type = PictureType.Composer
    # # x0C.Type = PictureType.Lyricist
    # # x0D.Type = PictureType.RecordingLocation
    # # x0E.Type = PictureType.DuringRecording
    # # x0F.Type = PictureType.DuringPerformance
    # # x10.Type = PictureType.MovieScreenCapture
    # # x11.Type = PictureType.ColoredFish
    # # x12.Type = PictureType.Illustration
    # # x13.Type = PictureType.BandLogo
    # # x14.Type = PictureType.PublisherLogo
    # # xff.Type = PictureType.NotAPicture
    # #
    # # clr.AddReference("System")
    # # from System import Array
    # #
    # # pictures = Array[AttachedPictureFrame]([AttachedPictureFrame(x) for x in [x00,x01,x02,x03,x04,x05,x06,x07,x08,x09,x0A,x0B,x0C,x0D,x0E,x0F,x10,x11,x12,x13,x14,xff]])
    # # FI.set_pictures(pictures)
    # # FI.file.Save()
