from Node import DoubleNode
from decorators import check_empty_list

class DoubleLinkedList:

	def __init__(self, nodes=None):
		self.head = None
		if nodes is not None:
			node = DoubleNode(data=nodes.pop(0))
			self.head = node
			for elem in nodes:
				node.next = DoubleNode(data=elem)
				prev_node = node
				node = node.next
				node.back = prev_node

	def __repr__(self):
		node = self.head
		nodes = ["None"]
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")

		return " <-> ".join(nodes)

	def __str__(self):
		node = self.head
		nodes = ["None"]
		while node is not None:
			nodes.append(str(node.data))
			node = node.next
		nodes.append("None")

		return " <-> ".join(nodes)

	def appendleft(self, node):
		node.next = self.head
		self.head.back = node
		self.head = node

	def appendright(self, node):
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
		current_node.next = node
		node.back = current_node

	@check_empty_list
	def appendafter(self, node_after, node):
		current_node = self.head
		while current_node.next is not None:
			if current_node.data == node_after.data:
				node.next = current_node.next
				node.back = current_node
				current_node.next.back = node
				current_node.next = node
				return
			current_node = current_node.next

		raise Exception(f"Node with data {node_after.data} not found.")

	@check_empty_list
	def appendbefore(self, node_before, node):
		if node_before.data == self.head.data:
			return self.appendleft(node)
		current_node = self.head
		while current_node.next is not None:
			if current_node.data == node_before.data:
				node.next = current_node
				node.back = current_node.back
				current_node.back.next = node
				current_node.back = node
				return
			current_node = current_node.next

		raise Exception(f"Node with data {node_before.data} not found.")

	@check_empty_list
	def pop(self, node):
		if node.data == self.head.data:
			self.head = self.head.next
			self.head.back = None
			return
		current_node = self.head
		while current_node.next is not None:
			if current_node.data == node.data:
				prev_node, next_node = current_node.back, current_node.next 
				prev_node.next = next_node
				next_node.back = prev_node
				return
			current_node = current_node.next

		raise Exception(f"Node with data {node_before.data} not found.")