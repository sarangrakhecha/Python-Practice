i=0
numbers = []

while i<6:
	print " At the top i is %d", i
	#i=int(raw_input(">"))  #even this is can be done.
	numbers.append(i)
	
	print "Numbers now : ",numbers
	print "At the bottom i is %d" %i
	i+=1

print "the numbers"

for num in numbers:
	print num