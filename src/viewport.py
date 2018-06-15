import sys
sys.path.append(r'C:\Python27\Lib')
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, FormBorderStyle, Form, Panel, BorderStyle, Label, Button, TextBox, DockStyle
from System.Drawing import Size, Color

window = Form()
window.Text = "tagme"
window.Name = "tagme"
window.Size = Size(500,500)
window.FormBorderStyle = FormBorderStyle.FixedDialog

LOAD_AREA = Panel()
#LOAD_AREA.BorderStyle = BorderStyle.FixedSingle
LOAD_AREA.Width = window.ClientRectangle.Width
LOAD_AREA.Height = 20
LOAD_AREA.Dock = DockStyle.Top
window.Controls.Add(LOAD_AREA)

test = Panel()
test.Width = LOAD_AREA.Width
test.Height = LOAD_AREA.Height
test.BorderStyle = BorderStyle.FixedSingle
test.Dock = DockStyle.Fill
test.BackColor = Color.Red
window.Controls.Add(test)

LOAD_BUTTON = Button()
LOAD_BUTTON.Text = "Load"
LOAD_BUTTON.Dock = DockStyle.Right
LOAD_TEXTBOX = TextBox()
LOAD_TEXTBOX.Dock = DockStyle.Left
LOAD_TEXTBOX.Width = LOAD_AREA.Width - LOAD_BUTTON.Width
LOAD_AREA.Controls.Add(LOAD_BUTTON)
LOAD_AREA.Controls.Add(LOAD_TEXTBOX)



Application.EnableVisualStyles()
Application.Run(window)


# window = Tk()
# window.title("Tagme")
# window.geometry("500x500")
#
# # Next level frames, the search bar area and a frame below it for the rest of the window
# LOAD_ROW = LabelFrame(MAIN_FRAME, height=20)
# LOAD_ROW.pack(side=TOP)
# MUTATION_AREA = LabelFrame(MAIN_FRAME)
# MUTATION_AREA.pack(side=BOTTOM, expand=1, fill=BOTH)
#
# # Widgets in the search area
# LOAD_BAR_TEXT = Label(LOAD_ROW, text="Path to file: ")
# LOAD_BAR = Entry(LOAD_ROW, width=70)
# LOAD_BAR_TEXT.pack(side=LEFT)
# LOAD_BAR.pack(side=RIGHT)
#
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
