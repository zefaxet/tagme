import sys
sys.path.append(r'C:\Python27\Lib')
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("System.IO")
clr.AddReference("System.Net")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, BorderStyle, Label, Button, TextBox, DockStyle, PictureBox, PictureBoxSizeMode, HorizontalAlignment
from System.Drawing import Size, Color, Image, Bitmap
from System.IO import MemoryStream
from System.Net import WebClient

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

#  LOAD FILE CONTROLS ###################
LOAD_BUTTON = Button()
LOAD_BUTTON.Text = "Load"
LOAD_BUTTON.Dock = DockStyle.Right

LOAD_TEXTBOX = TextBox()
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
UNDERLYING_INFORMATION_AREA.BackColor = Color.Black

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
COVER_ART.Image = Bitmap(MemoryStream(WebClient().DownloadData('https://upload.wikimedia.org/wikipedia/en/2/2c/Metallica_-_Metallica_cover.jpg')))
COVER_ART.Size = Size(160,160)
COVER_ART.Top = 45
COVER_ART.Left = (ART_AREA.Width - COVER_ART.Width) / 2

ART_AREA.Controls.Add(COVER_ART)
#########################################

#  INFO AREA CONTROLS ###################

#  Construct four identical textboxes
field = TextBox()
field.Width=250
field.Top=40
field.Left=20
field.Text="Name"
field.TextAlign = HorizontalAlignment.Center
INFO_AREA.Controls.Add(field)



Application.EnableVisualStyles()
Application.Run(window)



# # Mutation area frame split
# TOP_INFO = LabelFrame(MUTATION_AREA)
# TOP_INFO.pack(side=TOP, expand=1, fill=BOTH)
# LOWER_INFO = LabelFrame(MUTATION_AREA)
# LOWER_INFO.pack(side=BOTTOM, expand=1, fill=BOTH)
#
# # Top level frame split
# ART_FRAME = LabelFrame(TOP_INFO)
# ART_FRAME.master.size()
# ART_FRAME.pack(side=LEFT, expand=1, fill=BOTH, padx=5)
# TOP_INFO_ENTRY = LabelFrame(TOP_INFO)
# TOP_INFO_ENTRY.pack(side=RIGHT, expand=1, fill=BOTH)
# # COVER_ART = Label(MAIN_FRAME, bg="red", bitmap=Image(file="..//drawup.png"))
# # COVER_ART.pack(side=LEFT)
#
# window.mainloop()
