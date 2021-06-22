from Node import Node
from decorators import check_empty_list

class LinkedList:

	def __init__(self, nodes=None):
		self.head = None
		if nodes is not None:
			node = Node(data=nodes.pop(0))
			self.head = node
			for elem in nodes:
				node.next = Node(data=elem)
				node = node.next

	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return " -> ".join(nodes)

	def __str__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(str(node.data))
			node = node.next
		nodes.append("None")

		return " -> ".join(nodes)

	def appendleft(self, node):
		node.next = self.head
		self.head = node

	def appendright(self, node):
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
		current_node.next = node

	@check_empty_list
	def appendafter(self, node_after, node):
		current_node = self.head
		while current_node.next is not None:
			if current_node.data == node_after.data:
				node.next = current_node.next
				current_node.next = node
				return
			current_node = current_node.next

		raise Exception(f"Node with data {node_after.data} not found.")

	@check_empty_list
	def appendbefore(self, node_before, node):
		if node_before.data == self.head.data:
			return self.appendleft(node)
		current_node = self.head.next
		previous_node = self.head
		while current_node.next is not None:
			if current_node.data == node_before.data:
				node.next = current_node
				previous_node.next = node
				return
			previous_node = current_node
			current_node = current_node.next

		raise Exception(f"Node with data {node_before.data} not found.")

	@check_empty_list
	def pop(self, node):
		if node.data == self.head.data:
			self.head = self.head.next
			return
		current_node = self.head
		while current_node.next is not None:
			if current_node.next.data == node.data:
				current_node.next = current_node.next.next
				return
			current_node = current_node.next

		raise Exception(f"Node with data {node_before.data} not found.")


	@check_empty_list
	def popleft(self):
		node_to_delete = self.head
		self.head = self.head.next
		del node_to_delete

	@check_empty_list
	def popright(self):
		previous_node = self.head
		current_node = self.head.next
		while current_node.next is not None:
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = None
		del current_node
