from tkinter import *

window = Tk()
window.title("Tagme")
window.geometry("500x500")

FRAME = Frame(window)
FRAME.pack()

LOAD_ROW = LabelFrame(FRAME, height=20)
LOAD_ROW.pack(side=TOP)
LOAD_BAR_TEXT = Label(LOAD_ROW, text="Path to file: ")
LOAD_BAR = Entry(LOAD_ROW, width=70)
LOAD_BAR_TEXT.pack(side=LEFT)
LOAD_BAR.pack(side=RIGHT)

#COVER_ART = Label(FRAME, bg="red", bitmap=Image(file="..//drawup.png"))
#COVER_ART.pack(side=LEFT)

window.mainloop()
