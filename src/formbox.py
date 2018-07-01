import sys
sys.path.append(r'C:\Python27\Lib')
import clr
from log import create_logger

clr.AddReference("System")
from System import Array
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import TextBox, HorizontalAlignment
clr.AddReference("System.Drawing")
from System.Drawing import Color

class Formbox(TextBox):

    LOGGER = create_logger('Formbox')

    def __init__(self, placeholdertext, formtype=str):
        TextBox.__init__(self)
        self.Enter += self.receive_focus
        self.Leave += self.lose_focus
        self._placeholder = placeholdertext
        self._formtype = formtype

        self.lose_focus(None, None)

    def receive_focus(self, sender, args):
        if self.TextAlign == HorizontalAlignment.Center:
            self.Text = ""
            self.TextAlign = HorizontalAlignment.Left
            self.ForeColor = Color.Black
            if sender is self:
                self.LOGGER.debug("User focus on '{}' formbox".format(self._placeholder))

    def lose_focus(self, sender, args):
        if self.Text == "":
            self.Text = self._placeholder
            self.TextAlign = HorizontalAlignment.Center
            self.ForeColor = Color.Gray

    def get_text(self):
        if self.TextAlign == HorizontalAlignment.Center and self.Text == self._placeholder:
            return ""
        else:
            return self.Text

    def set_text(self, text):
        if not(text == "" or text is None):
            tag_type = type(text)
            if tag_type is str:
                self.receive_focus(None, None)
                self.Text = text
            elif tag_type is Array[str]:
                self.set_text(";".join(text))
            else:
                self.LOGGER.critical("Invalid typed object passed into set_text method.")
                raise TypeError("Unexpected object type {}. Expected type for field is {}"
                                .format(tag_type, self._formtype))
