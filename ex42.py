class Animal(object):
	def __init__(self,name,age):
		#self.name=name
		self.health=100
		self.age=age
		self.name=name
		print self.name
		print self.age
		#print self.asd
		print self.health
		

class Dog(Animal):
	def __init__(self,name, age,breed):
		super(Dog, self).__init__(name,age)
		self.name=name
		print self.age
		
rover=Dog("Pikachu",12,1230)
#rover=Dog("Pikachu1")