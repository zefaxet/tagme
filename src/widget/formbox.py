import sys

sys.path.append(r'C:\Python27\Lib')
import clr

from util.log import create_logger
from widget import init_widget

clr.AddReference("System")
from System import Array, UInt32

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import TextBox, HorizontalAlignment

clr.AddReference("System.Drawing")
from System.Drawing import Color


class FormboxTypes:
	STRING_TYPE = str
	STRING_ARRAY_TYPE = Array[str]
	INTEGER_TYPE = UInt32

	def __iter__(self):
		return [FormboxTypes.STRING_TYPE, FormboxTypes.STRING_ARRAY_TYPE, FormboxTypes.INTEGER_TYPE]


class Formbox(TextBox):
	# region Static members

	LOGGER = create_logger('Formbox')

	# endregion

	# region Constructor

	def __init__(self, parent, width, height, left_pad, top_pad, placeholder_text, form_type=str):
		TextBox.__init__(self)
		init_widget(self, parent, width, height, left_pad, top_pad)
		self.LOGGER.info("Initializing formbox '{}'.".format(placeholder_text))
		self.Enter += self.__receive_focus
		self.Leave += self.__lose_focus
		self.tag_getter_method = None
		self.tag_setter_method = None
		self.placeholder = placeholder_text
		self.form_type = form_type
		self.original = None

		#  Initalize formbox to placeholder text/styling
		self.__clear()

	# endregion

	# region Properties

	@property
	def form_type(self):
		return self._form_type

	@property
	def placeholder(self):
		return self._placeholder

	@form_type.setter
	def form_type(self, value):
		if value in FormboxTypes():
			self._form_type = value
		else:
			raise TypeError("Invalid formtype on form {}".format(self.placeholder))

	@placeholder.setter
	def placeholder(self, value):
		if not type(value) is str:
			raise TypeError("Non-string object as placeholder text.")
		else:
			self._placeholder = value

	# endregion

	# region Windows Forms Events

	def __receive_focus(self, sender, args):
		#  HAlign will only be centered if the form is in placeholder state
		if self.TextAlign == HorizontalAlignment.Center:
			self.__prepare()
		if sender is self:
			self.LOGGER.info("User focus on '{}' formbox".format(self.placeholder))

	def __lose_focus(self, sender, args):
		if self.Text == "":
			self.__clear()

	# endregion

	# region Class Methods

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
			return None
		else:
			text = self.Text

		if self.form_type is str:
			return text
		elif self.form_type is UInt32:
			self.LOGGER.info("Converting integer string {} in formbox '{}' to type UInt32.".format(text,
																								   self.placeholder))
			return UInt32(text)
		elif self.form_type is Array[str]:
			split_text = text.split(';')
			return Array[str](split_text)

	def set_text(self, text):
		if not (text == "" or text is None):
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
								.format(tag_type, self.placeholder, self.form_type))
		else:
			self.__clear()

	# endregion

	# region Private Methods

	def __clear(self):
		self.Text = self.placeholder
		self.TextAlign = HorizontalAlignment.Center
		self.ForeColor = Color.Gray

	def __prepare(self):
		self.Text = ""
		self.TextAlign = HorizontalAlignment.Left
		self.ForeColor = Color.Black

# endregion
