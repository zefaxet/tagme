class Widget:
	
	
	def __init__(self, parent, size, position):
		"""

		:type parent: 	System.Windows.Forms.Control
		:type size: 	System.Drawing.Size
		:type position: System.Drawing.Point
		"""
		self.parent = parent
		self.Size = size
		self.Location = position