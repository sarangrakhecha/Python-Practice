def add(a,b):
	print "Printing %d+%d : " %(a,b)
	return a+b
	
def sub(a,b):
	print "Printing %d-%d : " %(a,b)
	return a-b	

print "Function call"	
add1=add(int(raw_input("Insert value 1: ")),int(raw_input("Insert value 2: ")))
add2=add(2+3,4-6)
add3=add(float(raw_input("Insert Value 1: ")),float(raw_input("Insert value 2: ")))
sub1=sub(1,3)
sub2=sub(4,2)

print add1
print add2
print add3
print sub1
print sub2

