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
        self.LOGGER.info("Initializing formbox {}.".format(placeholdertext))
        self.Enter += self.__receive_focus
        self.Leave += self.__lose_focus
        self.tag_getter_method = None
        self.tag_setter_method = None
        self.placeholder = placeholdertext
        self.formtype = formtype
        self.original = None

        #  Initalize formbox to placeholder text/styling
        self.__clear()


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

    def __receive_focus(self, sender, args):
        #  HAlign will only be centered if the form is in placeholder state
        if self.TextAlign == HorizontalAlignment.Center:
            self.__prepare()
        if sender is self:
            self.LOGGER.info("User focus on '{}' formbox".format(self.placeholder))

    def __lose_focus(self, sender, args):
        if self.Text == "":
            self.__clear()

    ########################################

    #  CLASS METHODS #######################

    #  Sets the value for the formbox to default to on clear
    def setup(self, getter, setter):
        self.LOGGER.info("Extracting tag '{}': {}".format(self.placeholder,
                                                          "#NO TAG EXTRACTED#" if getter() is None else getter()))
        self.tag_getter_method = getter
        self.tag_setter_method = setter
        self.original = self.tag_getter_method()
        self.set_text(self.tag_getter_method())

    def apply(self):

        self.tag_setter_method(self.get_text())

    def get_text(self):
        if self.TextAlign == HorizontalAlignment.Center and self.Text == self.placeholder:
            text = None
        else:
            text = self.Text

        if self.formtype is str:
            return text
        elif self.formtype is UInt32:
            self.LOGGER.info("Converting integer string {} in formbox '{}' to type UInt32.".format(text,
                                                                                                 self.placeholder))
            return UInt32(text)
        elif self.formtype is Array[str]:
            split_text = text.split(';')
            return Array[str](split_text)

    def set_text(self, text):
        if not(text == "" or text is None):
            tag_type = type(text)

            #  clear placeholder formatting
            self.__prepare()

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
            self.__clear()

    ########################################

    #  PRIVATE METHODS #####################

    def __clear(self):
        self.Text = self.placeholder
        self.TextAlign = HorizontalAlignment.Center
        self.ForeColor = Color.Gray

    def __prepare(self):
        self.Text = ""
        self.TextAlign = HorizontalAlignment.Left
        self.ForeColor = Color.Black