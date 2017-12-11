class Parent(object):
	def override(self):
		print"In Parent"
		
class Child(Parent):
	def override(self):
		print "In Child"
		
dad=Parent()
son=Child()

dad.override()
son.override()
