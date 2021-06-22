class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return self.data

	def __str__(self):
		return f"{self.data}"

class DoubleNode(Node):

	def __init__(self, data):
		super().__init__(data)
		self.back = None