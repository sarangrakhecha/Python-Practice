class Parent(object):
	def alter(self):
		print "In parent class"
		
class Child(Parent):
	def alter(self):
		print "In child before super"
	#	super(Child, self).alter()
		print "In child after super "
	
dad=Parent()  
son=Child()   

dad.alter()    
son.alter()	
		