# region Imports

# region .NET Imports
import clr

# clr.AddReference("System")
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, Button, DockStyle, PictureBox, PictureBoxSizeMode, \
    MessageBox, MessageBoxButtons, DialogResult, \
    ComboBox, ComboBoxStyle

# TODO Add icon for taskbar and form if possible
clr.AddReference("System.Drawing")
from System.Drawing import Size, Color, Bitmap#, Icon

clr.AddReference("System.IO")
from System.IO import MemoryStream


# endregion

# region Python/Project Imports

import sys
from util.log import create_logger
from widget.formbox import Formbox
from FileInterface import FileInterface

# endregion

# endregion

sys.path.append(r'C:\Python27\Lib')

LOGGER = create_logger('Viewport')
FORMBOXES = {}
ART_SELECTOR_LIST_ITEMS = ["Front Cover", "Back Cover"]
FI = None

LOGGER.info("Booting viewport.")

window = Form()
window.Text = "tagme"
window.Name = "tagme"
window.Size = Size(500, 300)
window.FormBorderStyle = FormBorderStyle.FixedDialog

#  TOP LEVEL CONTROLS ###################
LOAD_AREA = Panel()
# LOAD_AREA.BorderStyle = BorderStyle.FixedSingle
LOAD_AREA.Width = window.ClientRectangle.Width
LOAD_AREA.Height = 20
LOAD_AREA.Dock = DockStyle.Top
window.Controls.Add(LOAD_AREA)

MUTATION_AREA = Panel()
MUTATION_AREA.Width = LOAD_AREA.Width
MUTATION_AREA.Height = LOAD_AREA.Height
# MUTATION_AREA.BorderStyle = BorderStyle.FixedSingle
MUTATION_AREA.Dock = DockStyle.Fill
# MUTATION_AREA.BackColor = Color.Red
window.Controls.Add(MUTATION_AREA)
#########################################

#  LOAD FILE CONTROLS ###################

# TODO load button becomes "Unload" if file is loaded and the textbox is empty
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
# INFO_AREA.BackColor = Color.Blue

EXPLORER_VISIBLE_INFORMATION_AREA.Controls.Add(ART_AREA)
EXPLORER_VISIBLE_INFORMATION_AREA.Controls.Add(INFO_AREA)
#########################################

# TODO add dropdown to modify each of the album art tags
#  ART AREA CONTROLS ####################
ART_SELECTOR = ComboBox()
ART_SELECTOR.Size = Size(100, 20)
ART_SELECTOR.Top = 26
ART_SELECTOR.Left = (ART_AREA.Width - ART_SELECTOR.Width) / 2
ART_SELECTOR.DropDownStyle = ComboBoxStyle.DropDownList
for item in ART_SELECTOR_LIST_ITEMS:
    ART_SELECTOR.Items.Add(item)
ART_SELECTOR.SelectedItem = ART_SELECTOR.Items[0]
ART_SELECTOR.Enabled = False

# TODO Create new class for this widget
ART = PictureBox()
ART.SizeMode = PictureBoxSizeMode.StretchImage
ART.BackColor = Color.White
ART.Size = Size(160, 160)
ART.Top = 50
ART.Left = (ART_AREA.Width - ART.Width) / 2

ART_AREA.Controls.Add(ART_SELECTOR)
ART_AREA.Controls.Add(ART)
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
APPLY_BUTTON.Enabled = False
UNDERLYING_INFORMATION_AREA.Controls.Add(APPLY_BUTTON)

FETCH_BUTTON = Button()
FETCH_BUTTON.Text = "Tagme"
FETCH_BUTTON.Left = 100
FETCH_BUTTON.Enabled = False
UNDERLYING_INFORMATION_AREA.Controls.Add(FETCH_BUTTON)


#  Button Methods #######################


def load_file(sender, args):
    global FI
    APPLY_BUTTON.Enabled, FETCH_BUTTON.Enabled = [True] * 2
    path = LOAD_TEXTBOX.get_text()
    if path:
        LOGGER.info("Loading file: {}".format(path))
        FI = FileInterface(path)
        LOGGER.info(r"'{}' loaded. Extracting tags.".format(path))

        FORMBOXES["Title"].setup(FI.get_title, FI.set_title)
        FORMBOXES["Album"].setup(FI.get_album, FI.set_album)
        FORMBOXES["Album Artist"].setup(FI.get_main_artist, FI.set_main_artist)
        FORMBOXES["Contributing Artists"].setup(FI.get_performers, FI.set_performers)
        FORMBOXES["Genre"].setup(FI.get_genre, FI.set_genre)
        FORMBOXES["Year"].setup(FI.get_year, FI.set_year)
        FORMBOXES["Track #"].setup(FI.get_track_number, FI.set_track_number)

        try:
            bitmap = Bitmap(MemoryStream(FI.get_pictures()[0].Data.Data))
        except IndexError:
            # TODO add placeholder bitmap for empty art
            bitmap = None

        ART.Image = bitmap

def apply_changes(sender, args):
    changed_forms = []
    for form in FORMBOXES.keys():
        box = FORMBOXES[form]
        if box.get_text() != box.original:
            LOGGER.info("Change found in formbox '{}': '{}' -> '{}'".format(box.placeholder,
                                                                            box.original, box.get_text()))
            changed_forms.append(form)
        changed_forms.reverse()
    if len(changed_forms):
        response = MessageBox.Show(
            "Are you sure that you want to apply the changes made? Changes have occurred to the following tags: {}"
            .format(", ".join(changed_forms)), "Confirm changes", MessageBoxButtons.YesNo)
        if response == DialogResult.Yes:
            LOGGER.info("Applying changes...")
            for form in changed_forms:
                box = FORMBOXES[form]
                LOGGER.info("Applying change in formbox '{}': '{}' -> '{}'".format(box.placeholder,
                                                                                   box.original, box.get_text()))
                box.apply()
            FI.file.Save()
        elif response == DialogResult.No:
            print "nah"
    else:
        MessageBox.Show(
            "There are no changes to apply.", "Confirm changes"
        )


def tagme(sender, args):
    clr.AddReference("System.Net")
    from System.Net import WebClient
    ART.Image = Bitmap(MemoryStream(WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg')))

#  ComboBox Events ######################


def update_art(sender, args):
    # TODO add placeholder bitmap for empty art
    # TODO update art based on status of selector
    LOGGER.info("Selected file art changed to '{}'.".format(sender.SelectedItem))
    #bitmap = Bitmap(MemoryStream())
    #ART.Image


LOAD_BUTTON.Click += load_file
APPLY_BUTTON.Click += apply_changes
FETCH_BUTTON.Click += tagme

ART_SELECTOR.SelectedValueChanged += update_art

LOAD_TEXTBOX.set_text(r'../test/Roundabout.flac')

Application.EnableVisualStyles()
Application.Run(window)

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