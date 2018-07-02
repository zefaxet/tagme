import sys
sys.path.append(r'C:\Python27\Lib')
import clr
from log import create_logger

clr.AddReference("System")
from System import Array, UInt32
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import TextBox, HorizontalAlignment
clr.AddReference("System.Drawing")
from System.Drawing import Color


class Formbox(TextBox):

    LOGGER = create_logger('Formbox')
    VALID_TYPES = [str, Array[str], UInt32]

    def __init__(self, placeholdertext, formtype=str):
        TextBox.__init__(self)
        self.Enter += self.receive_focus
        self.Leave += self.lose_focus
        self._placeholder = placeholdertext
        self.formtype = formtype

        self.lose_focus(None, None)

        self.LOGGER.info("Initializing formbox {}.".format(self.placeholder))

    #  FIELDS ##############################

    @property
    def formtype(self):
        return self._formtype

    @property
    def placeholder(self):
        return self._placeholder

    @formtype.setter
    def formtype(self, value):
        if value in self.VALID_TYPES:
            self._formtype = value
        else:
            raise TypeError("Invalid formtype on form {}".format(self.placeholder))

    @placeholder.setter
    def placeholder(self, value):
        if not type(value) is str:
            raise TypeError("Non-string object as placeholder text.")
        else:
            self._placeholder = value

    ########################################

    #  WINDOWS FORMS EVENTS ################

    def receive_focus(self, sender, args):
        if self.TextAlign == HorizontalAlignment.Center:
            self.Text = ""
            self.TextAlign = HorizontalAlignment.Left
            self.ForeColor = Color.Black
        if sender is self:
            self.LOGGER.info("User focus on '{}' formbox".format(self.placeholder))

    def lose_focus(self, sender, args):
        if self.Text == "":
            self.Text = self._placeholder
            self.TextAlign = HorizontalAlignment.Center
            self.ForeColor = Color.Gray

    ########################################

    #  CLASS METHODS #######################

    def get_text(self):
        if self.TextAlign == HorizontalAlignment.Center and self.Text == self.placeholder:
            text = ""
        else:
            text = self.Text

        if self.formtype is str:
            return text
        elif self.formtype is Array[str]:
            split_text = text.split(';')
            return Array[str](split_text)

    def set_text(self, text):
        if not(text == "" or text is None):
            tag_type = type(text)
            self.receive_focus(None, None)
            if tag_type is str:
                self.Text = text
            elif tag_type is UInt32:
                self.LOGGER.info("Formbox '{}' recieved UInt32, {}. Casting to str.".format(self.placeholder, text))
                self.Text = str(text)
            elif tag_type is Array[str]:
                self.set_text(";".join(text))
            else:
                self.LOGGER.critical("Invalid typed object passed into set_text method.")
                raise TypeError("Unexpected object type {} in formbox '{}'. Expected type for field is {}"
                                .format(tag_type, self.placeholder, self.formtype))
        else:
            self.lose_focus(None, None)
