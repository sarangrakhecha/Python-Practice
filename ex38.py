ten_things="a b c d e f"

print "go till 10"

stuff=ten_things.split(' ')
print stuff

more_stuff  = ["g","h","i","j","k"]

while len(stuff)!=10:
	extra_stuff=more_stuff.pop()
	print "\nextra stuff : ",extra_stuff
	stuff.append(extra_stuff)
	print "appended stuff : ",stuff
	more_stuff.append("100")
	print "more stuff : ",more_stuff

trial = [1,2,3,4,5]
i=0
while i!=5:
		try1=trial.pop()
		trial.append(try1)
		i=i+1
print "\ntrial is : ",trial
trial.append(732)
print trial

print stuff
print stuff[0]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])