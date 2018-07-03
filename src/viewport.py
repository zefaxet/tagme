import sys
sys.path.append(r'C:\Python27\Lib')
import clr
from log import create_logger

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, BorderStyle, Label, Button, TextBox, DockStyle, PictureBox, PictureBoxSizeMode, HorizontalAlignment
clr.AddReference("System.Drawing")
from System.Drawing import Size, Color, Image, Bitmap
clr.AddReference("System.IO")
from System.IO import MemoryStream
clr.AddReference("System.Net")
from System.Net import WebClient

from formbox import Formbox
from FileInterface import FileInterface

LOGGER = create_logger('Viewport')
FORMBOXES = {}
FI = None

LOGGER.info("Booting viewport.")

window = Form()
window.Text = "tagme"
window.Name = "tagme"
window.Size = Size(500,300)
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

#  LOAD FILE CONTROLS ###################

LOAD_BUTTON = Button()
LOAD_BUTTON.Text = "Load"
LOAD_BUTTON.Dock = DockStyle.Right

LOAD_TEXTBOX = Formbox("Path to file...")
LOAD_TEXTBOX.Dock = DockStyle.Left
LOAD_TEXTBOX.Width = LOAD_AREA.Width - LOAD_BUTTON.Width

LOAD_AREA.Controls.Add(LOAD_BUTTON)
LOAD_AREA.Controls.Add(LOAD_TEXTBOX)
#########################################

#  MUTATION AREA CONTROLS ###############
EXPLORER_VISIBLE_INFORMATION_AREA = Panel()
EXPLORER_VISIBLE_INFORMATION_AREA.Height = MUTATION_AREA.Height * 6 / 7
EXPLORER_VISIBLE_INFORMATION_AREA.Dock = DockStyle.Top

UNDERLYING_INFORMATION_AREA = Panel()
UNDERLYING_INFORMATION_AREA.Height = MUTATION_AREA.Height * 1 / 7
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
#COVER_ART.Image = Bitmap(FileInterface(r'../test/Blackened.mp3').GetPicture)
COVER_ART.BackColor = Color.White
COVER_ART.Size = Size(160,160)
COVER_ART.Top = 45
COVER_ART.Left = (ART_AREA.Width - COVER_ART.Width) / 2

ART_AREA.Controls.Add(COVER_ART)
#########################################

#  INFO AREA CONTROLS ###################

#  Construct four identical textboxes
#  Each Formbox is 40 units above the next
FORMBOXES["Title"] = Formbox("Title")
FORMBOXES["Title"].Width = 250
FORMBOXES["Title"].Top = 35
FORMBOXES["Title"].Left = 20
INFO_AREA.Controls.Add(FORMBOXES["Title"])

FORMBOXES["Album"] = Formbox("Album")
FORMBOXES["Album"].Width = 250
FORMBOXES["Album"].Top = 75
FORMBOXES["Album"].Left = 20
INFO_AREA.Controls.Add(FORMBOXES["Album"])

FORMBOXES["Album Artist"] = Formbox("Main Artist")
FORMBOXES["Album Artist"].Width = 250
FORMBOXES["Album Artist"].Top = 115
FORMBOXES["Album Artist"].Left = 20
INFO_AREA.Controls.Add(FORMBOXES["Album Artist"])

FORMBOXES["Contributing Artists"] = Formbox("Contributing Artist(s)", Formbox.VALID_TYPES[1])
FORMBOXES["Contributing Artists"].Width = 250
FORMBOXES["Contributing Artists"].Top = 155
FORMBOXES["Contributing Artists"].Left = 20
INFO_AREA.Controls.Add(FORMBOXES["Contributing Artists"])

FORMBOXES["Genre"] = Formbox("Genre", Formbox.VALID_TYPES[1])
FORMBOXES["Genre"].Width = 250
FORMBOXES["Genre"].Top = 195
FORMBOXES["Genre"].Left = 20
INFO_AREA.Controls.Add(FORMBOXES["Genre"])
#########################################

#  UNDERLYING INFORMATION AREA CONTROLS #
FORMBOXES["Year"] = Formbox("Year", Formbox.VALID_TYPES[2])
FORMBOXES["Year"].Top = 10
FORMBOXES["Year"].Left = UNDERLYING_INFORMATION_AREA.Width - 270
UNDERLYING_INFORMATION_AREA.Controls.Add(FORMBOXES["Year"])

FORMBOXES["Track #"] = Formbox("Track #", Formbox.VALID_TYPES[2])
FORMBOXES["Track #"].Top = 10
FORMBOXES["Track #"].Left = UNDERLYING_INFORMATION_AREA.Width - 120
UNDERLYING_INFORMATION_AREA.Controls.Add(FORMBOXES["Track #"])

APPLY_BUTTON = Button()
APPLY_BUTTON.Text = "Apply"
APPLY_BUTTON.Left = 15
UNDERLYING_INFORMATION_AREA.Controls.Add(APPLY_BUTTON)

FETCH_BUTTON = Button()
FETCH_BUTTON.Text = "Tagme"
FETCH_BUTTON.Left = 100
UNDERLYING_INFORMATION_AREA.Controls.Add(FETCH_BUTTON)

#  Button Methods #######################


def load_file(object, sender):

    path = LOAD_TEXTBOX.get_text()
    if path:
        LOGGER.info("Loading file: {}".format(path))
        FI = FileInterface(path)
        LOGGER.info(r"'{}' loaded. Extracting tags.".format(path))

        FORMBOXES["Title"].setup(FI.get_title())
        FORMBOXES["Album"].setup(FI.get_album())
        FORMBOXES["Album Artist"].setup(FI.get_main_artist())
        FORMBOXES["Contributing Artists"].setup(FI.get_performers())
        FORMBOXES["Genre"].setup(FI.get_genre())
        FORMBOXES["Year"].setup(FI.get_year())
        FORMBOXES["Track #"].setup(FI.get_track_number())
        

def apply_changes(object, sender):
    LOGGER.info("Applying changes...")
    global FI
    for form in FORMBOXES.keys():
        box = FORMBOXES[form]
        print box.get_text() == box.original, box.placeholder
    #FI.file.Save()


def tagme(object, sender):
    print FORMBOXES["Album"].get_text()


LOAD_BUTTON.Click += load_file
APPLY_BUTTON.Click += apply_changes
FETCH_BUTTON.Click += tagme

LOAD_TEXTBOX.set_text(r'../test/Blackened.mp3')

Application.EnableVisualStyles()
Application.Run(window)

