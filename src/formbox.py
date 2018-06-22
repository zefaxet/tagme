import sys
sys.path.append(r'C:\Python27\Lib')
import clr

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import TextBox, HorizontalAlignment
clr.AddReference("System.Drawing")
from System.Drawing import Color

class Formbox(TextBox):

    def __init__(self, placeholdertext):
        TextBox.__init__(self)
        self.Enter += self.recieve_focus
        self.Leave += self.lose_focus
        self.__placeholder = placeholdertext
        self.lose_focus(None, None)


    def recieve_focus(self, sender, args):
        if self.TextAlign == HorizontalAlignment.Center:
            self.Text = ""
            self.TextAlign = HorizontalAlignment.Left
            self.ForeColor = Color.Black

    def lose_focus(self, sender, args):
        if self.Text == "":
            self.Text = self.__placeholder
            self.TextAlign = HorizontalAlignment.Center
            self.ForeColor = Color.Gray

    def GetText(self):
        if self.TextAlign == HorizontalAlignment.Center and self.Text == self.__placeholder:
            return ""
        else:
            return self.Text