

# The purpose of this method is to get around ipy's limitations regarding multiple
# inheritance between CLR and pure python classes
def init_widget(self, parent, width, height, left_pad, top_pad):
	"""
	:type self:		System.Windows.Forms.Control
	:type parent: 	System.Windows.Forms.Control
	:type width: 	int
	:type height: 	int
	:type left_pad:	int, Nullable
	:type top_pad:	int, Nullable
	"""
	self.parent = parent
	if width:
		self.Width = width
	if height:
		self.Height = height
	self.Left = left_pad
	self.Top = top_pad

	parent.Controls.Add(self)
