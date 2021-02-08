class Hello:
	def __init__(self, name):
		self.name = name

	def demo_fun(self):
		return f" Hello {self.name}"


if __name__ == '__main__':
	obj = Hello('Birajit')
	print(obj.demo_fun())
