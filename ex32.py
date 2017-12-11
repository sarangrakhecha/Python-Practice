count=[1,2,3,4,5]
fruits=['appple','banana','grapes']
mix=[1,'sarang',3,'rakhecha','rajendra',2,4,5]

#print"list : ",mix

for number in count:
	print "This is count list : ",number
	#print "This is count list %d: " %number
	
for fruits in fruits:
	print "these are fruits : ",fruits
	#print "These are fruits %s" %fruits
	
for i in mix:
	print "Mix is : %r" %mix
	
elements=[]

for i in range(0,5),:   	#if we put a comma, it will itearte only once.
	i=int(raw_input("insert in element : ")) #type-casting required
	print " Adding %d in list " %i
	elements.append(i)
	
for i in range(0,5): #will go from 0,1,2,3,4
	print " Adding %d in list " %i
	elements.append(i)
	
for i in elements:
	print "elements : %d" %i