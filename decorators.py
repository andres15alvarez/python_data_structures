def check_empty_list(fn):
	def wrapper(self, *args, **kwargs):
		if self.head is None:
			raise Exception("List is empty")
		fn(self, *args, **kwargs)

	return wrapper