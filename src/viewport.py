from tkinter import *

window = Tk()
window.title("Tagme")
window.geometry("500x500")

# Top level frame, whole window
MAIN_FRAME = Frame(window)
MAIN_FRAME.pack(expand=1, fill=BOTH)

# Next level frames, the search bar area and a frame below it for the rest of the window
LOAD_ROW = LabelFrame(MAIN_FRAME, height=20)
LOAD_ROW.pack(side=TOP)
MUTATION_AREA = LabelFrame(MAIN_FRAME)
MUTATION_AREA.pack(side=BOTTOM, expand=1, fill=BOTH)

# Widgets in the search area
LOAD_BAR_TEXT = Label(LOAD_ROW, text="Path to file: ")
LOAD_BAR = Entry(LOAD_ROW, width=70)
LOAD_BAR_TEXT.pack(side=LEFT)
LOAD_BAR.pack(side=RIGHT)

# Mutation area frame split
TOP_INFO = LabelFrame(MUTATION_AREA)
TOP_INFO.pack(side=TOP, expand=1, fill=BOTH)
LOWER_INFO = LabelFrame(MUTATION_AREA)
LOWER_INFO.pack(side=BOTTOM, expand=1, fill=BOTH)

# Top level frame split
ART_FRAME = LabelFrame(TOP_INFO)
ART_FRAME.master.size()
ART_FRAME.pack(side=LEFT, expand=1, fill=BOTH, padx=5)
TOP_INFO_ENTRY = LabelFrame(TOP_INFO)
TOP_INFO_ENTRY.pack(side=RIGHT, expand=1, fill=BOTH)
# COVER_ART = Label(MAIN_FRAME, bg="red", bitmap=Image(file="..//drawup.png"))
# COVER_ART.pack(side=LEFT)

window.mainloop()
