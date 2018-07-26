# region Imports

# region .NET Imports
import clr

# clr.AddReference("System")
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, Button, DockStyle, PictureBox, \
	PictureBoxSizeMode, \
	MessageBox, MessageBoxButtons, DialogResult, \
	ComboBox, ComboBoxStyle

# TODO Add icon for taskbar and form if possible
clr.AddReference("System.Drawing")
from System.Drawing import Size, Color, Bitmap  # , Icon

clr.AddReference("System.IO")
from System.IO import MemoryStream

# endregion

# region Python/Project Imports

import sys
from util.log import create_logger
from widget.formbox import Formbox, FormboxTypes
from widget.art import *
from FileInterface import FileInterface

# endregion

# endregion

sys.path.append(r'C:\Python27\Lib')

LOGGER = create_logger('Viewport')
FORMBOXES = {}
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

load_box_width = LOAD_AREA.Width - LOAD_BUTTON.Width

LOAD_TEXTBOX = Formbox(LOAD_AREA, load_box_width, None, 0, 0, "Path to File...")
LOAD_TEXTBOX.Dock = DockStyle.Left

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

#  ART AREA CONTROLS ####################
ART_SELECTOR = Selector(ID3_TAGS.keys(), Size(100, 20), 26, (ART_AREA.Width - 100) / 2)

# TODO finish art widget
ART = Art(ART_AREA)
# TODO Apply functionality to art widget class
#  ART.Image = Bitmap(MemoryStream(WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg')))

ART_AREA.Controls.Add(ART_SELECTOR)
#########################################

#  INFO AREA CONTROLS ###################

#  Construct four identical textboxes
#  Each Formbox is 40 units above the next
FORMBOXES["Title"] = Formbox(INFO_AREA, 250, None, 20, 35, "Title")

FORMBOXES["Album"] = Formbox(INFO_AREA, 250, None, 20, 75, "Album")

FORMBOXES["Album Artist"] = Formbox(INFO_AREA, 250, None, 20, 115, "Main Artist")

FORMBOXES["Contributing Artists"] = Formbox(INFO_AREA, 250, None, 20, 155, "Contributing Artist(s)",
											FormboxTypes.STRING_ARRAY_TYPE)

FORMBOXES["Genre"] = Formbox(INFO_AREA, 250, None, 20, 195, "Genre", FormboxTypes.STRING_ARRAY_TYPE)
#########################################

#  UNDERLYING INFORMATION AREA CONTROLS #
yearbox_left_pad = UNDERLYING_INFORMATION_AREA.Width - 270
FORMBOXES["Year"] = Formbox(UNDERLYING_INFORMATION_AREA, None, None, yearbox_left_pad, 10, "Year",
							FormboxTypes.INTEGER_TYPE)

tracknum_left_pad = UNDERLYING_INFORMATION_AREA.Width - 120
FORMBOXES["Track #"] = Formbox(UNDERLYING_INFORMATION_AREA, None, None, tracknum_left_pad, 10, "Track #", FormboxTypes.INTEGER_TYPE)

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


def load_file(sender, args) :
	global FI
	APPLY_BUTTON.Enabled, FETCH_BUTTON.Enabled = [True] * 2
	path = LOAD_TEXTBOX.get_text()
	if path :
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

		try :
			bitmap = Bitmap(MemoryStream(FI.get_pictures()[0].Data.Data))
		except IndexError :
			# TODO add placeholder bitmap for empty art
			bitmap = None

		ART.Image = bitmap


def apply_changes(sender, args) :
	changed_forms = []
	for form in FORMBOXES.keys() :
		box = FORMBOXES[form]
		if box.get_text() != box.original :
			LOGGER.info("Change found in formbox '{}': '{}' -> '{}'".format(box.placeholder,
																			box.original, box.get_text()))
			changed_forms.append(form)
		changed_forms.reverse()
	if len(changed_forms) :
		response = MessageBox.Show(
			"Are you sure that you want to apply the changes made? Changes have occurred to the following tags: {}"
				.format(", ".join(changed_forms)), "Confirm changes", MessageBoxButtons.YesNo)
		if response == DialogResult.Yes :
			LOGGER.info("Applying changes...")
			for form in changed_forms :
				box = FORMBOXES[form]
				LOGGER.info("Applying change in formbox '{}': '{}' -> '{}'".format(box.placeholder,
																				   box.original, box.get_text()))
				box.apply()
			FI.file.Save()
		elif response == DialogResult.No :
			print "nah"
	else :
		MessageBox.Show(
			"There are no changes to apply.", "Confirm changes"
		)


def tagme(sender, args) :
	clr.AddReference("System.Net")
	from System.Net import WebClient
	ART.Image = Bitmap(MemoryStream(
		WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg')))


#  ComboBox Events ######################


def update_art(sender, args) :
	# TODO add placeholder bitmap for empty art
	# TODO update art based on status of selector
	LOGGER.info("Selected file art changed to '{}'.".format(sender.SelectedItem))


# bitmap = Bitmap(MemoryStream())
# ART.Image


LOAD_BUTTON.Click += load_file
APPLY_BUTTON.Click += apply_changes
FETCH_BUTTON.Click += tagme

ART_SELECTOR.SelectedValueChanged += update_art

LOAD_TEXTBOX.set_text(r'../test/Roundabout.flac')

Application.EnableVisualStyles()
Application.Run(window)
