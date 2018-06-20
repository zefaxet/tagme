import sys
sys.path.append(r'C:\Python27\Lib')
import clr

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import TextBox

class formbox(TextBox):

    def __init__(self, placeholdertext):
        TextBox.__init__(self)
        self.Text = placeholdertext