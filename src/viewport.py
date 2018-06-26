import sys
sys.path.append(r'C:\Python27\Lib')

import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, BorderStyle, Label, Button, TextBox, DockStyle, PictureBox, PictureBoxSizeMode, HorizontalAlignment
clr.AddReference("System.Drawing")
from System.Drawing import Size, Color, Image, Bitmap
clr.AddReference("System.IO")
from System.IO import MemoryStream
clr.AddReference("System.Net")
from System.Net import WebClient

from formbox import Formbox
from TagExtract import FileInterface

window = Form()
window.Text = "tagme"
window.Name = "tagme"
window.Size = Size(500,500)
window.FormBorderStyle = FormBorderStyle.FixedDialog

#  TOP LEVEL CONTROLS ###################
LOAD_AREA = Panel()
#LOAD_AREA.BorderStyle = BorderStyle.FixedSingle
LOAD_AREA.Width = window.ClientRectangle.Width
LOAD_AREA.Height = 20
LOAD_AREA.Dock = DockStyle.Top
window.Controls.Add(LOAD_AREA)

MUTATION_AREA = Panel()
MUTATION_AREA.Width = LOAD_AREA.Width
MUTATION_AREA.Height = LOAD_AREA.Height
#MUTATION_AREA.BorderStyle = BorderStyle.FixedSingle
MUTATION_AREA.Dock = DockStyle.Fill
#MUTATION_AREA.BackColor = Color.Red
window.Controls.Add(MUTATION_AREA)
#########################################

def Extract(sender, args):
    path = LOAD_TEXTBOX.GetText()


#  LOAD FILE CONTROLS ###################
LOAD_BUTTON = Button()
LOAD_BUTTON.Text = "Load"
LOAD_BUTTON.Dock = DockStyle.Right
LOAD_BUTTON.Click += Extract

LOAD_TEXTBOX = Formbox("Path to file...")
LOAD_TEXTBOX.Dock = DockStyle.Left
LOAD_TEXTBOX.Width = LOAD_AREA.Width - LOAD_BUTTON.Width

LOAD_AREA.Controls.Add(LOAD_BUTTON)
LOAD_AREA.Controls.Add(LOAD_TEXTBOX)
#########################################

#  MUTATION AREA CONTROLS ###############
EXPLORER_VISIBLE_INFORMATION_AREA = Panel()
EXPLORER_VISIBLE_INFORMATION_AREA.Height = MUTATION_AREA.Height / 2
EXPLORER_VISIBLE_INFORMATION_AREA.Dock = DockStyle.Top

UNDERLYING_INFORMATION_AREA = Panel()
UNDERLYING_INFORMATION_AREA.Height = MUTATION_AREA.Height / 2
UNDERLYING_INFORMATION_AREA.Dock = DockStyle.Bottom

MUTATION_AREA.Controls.Add(UNDERLYING_INFORMATION_AREA)
MUTATION_AREA.Controls.Add(EXPLORER_VISIBLE_INFORMATION_AREA)
#########################################

#  EXPLORER INFO AREA CONTROLS ##########
ART_AREA = Panel()
ART_AREA.Width = EXPLORER_VISIBLE_INFORMATION_AREA.Width * 0.4
ART_AREA.Dock = DockStyle.Left

INFO_AREA = Panel()
INFO_AREA.Width = EXPLORER_VISIBLE_INFORMATION_AREA.Width * 0.6
INFO_AREA.Dock = DockStyle.Right
#INFO_AREA.BackColor = Color.Blue

EXPLORER_VISIBLE_INFORMATION_AREA.Controls.Add(ART_AREA)
EXPLORER_VISIBLE_INFORMATION_AREA.Controls.Add(INFO_AREA)
#########################################

#  ART AREA CONTROLS ####################
COVER_ART = PictureBox()
COVER_ART.SizeMode = PictureBoxSizeMode.StretchImage
#COVER_ART.Image = Bitmap(MemoryStream(WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg')))
COVER_ART.Image = Bitmap(FileInterface(r'../test/Blackened.mp3').GetPicture)
COVER_ART.Size = Size(160,160)
COVER_ART.Top = 45
COVER_ART.Left = (ART_AREA.Width - COVER_ART.Width) / 2

ART_AREA.Controls.Add(COVER_ART)
#########################################

#  INFO AREA CONTROLS ###################

#  Construct four identical textboxes
#  Each Formbox is 40 units above the next
TITLE_FIELD = Formbox("Title")
TITLE_FIELD.Width = 250
TITLE_FIELD.Top = 35
TITLE_FIELD.Left = 20
INFO_AREA.Controls.Add(TITLE_FIELD)

ALBUM_FIELD = Formbox("Album")
ALBUM_FIELD.Width = 250
ALBUM_FIELD.Top = 75
ALBUM_FIELD.Left = 20
INFO_AREA.Controls.Add(ALBUM_FIELD)

MAIN_ARTIST = Formbox("Main Artist")
MAIN_ARTIST.Width = 250
MAIN_ARTIST.Top = 115
MAIN_ARTIST.Left = 20
INFO_AREA.Controls.Add(MAIN_ARTIST)

CONTRIBUTING_ARTISTS = Formbox("Contributing Artist(s)")
CONTRIBUTING_ARTISTS.Width = 250
CONTRIBUTING_ARTISTS.Top = 155
CONTRIBUTING_ARTISTS.Left = 20
INFO_AREA.Controls.Add(CONTRIBUTING_ARTISTS)

GENRE = Formbox("Genre")
GENRE.Width = 250
GENRE.Top = 195
GENRE.Left = 20
INFO_AREA.Controls.Add(GENRE)
#########################################

#  UNDERLYING INFORMATION AREA CONTROLS #
DEBUT_YEAR = Formbox("Year")
DEBUT_YEAR.Top = 10
DEBUT_YEAR.Left = 20
UNDERLYING_INFORMATION_AREA.Controls.Add(DEBUT_YEAR)

TRACK = Formbox("Track #")
TRACK.Top = 10
TRACK.Left = 140
UNDERLYING_INFORMATION_AREA.Controls.Add(TRACK)


Application.EnableVisualStyles()
Application.Run(window)