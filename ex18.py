def print_two(*args):
	args1,args2=args
	print "args1 : %r  args2: %r" %(args1,args2)

def print_two_again(arg1,arg2):
	print "args1 : %r \n args2: %r" %(arg1,arg2)
	
def print_one(arg1):
	print "args1 :  ",arg1
	
def print_zero():
	print "Nothing"
	
print_two("Sarang","Rakhecha")
print_two_again("James","Bond")
print_one("James")
print_zero()