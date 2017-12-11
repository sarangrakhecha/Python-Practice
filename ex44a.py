class Parent(object):
	def implicit(self):
		print"Hey there!"

class Child(Parent):
	pass

dad=Parent()
son=Child()

dad.implicit()
son.implicit()