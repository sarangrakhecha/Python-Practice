from sys import argv

#script, filename=argv

#txt=open(filename)

#print"Name of your file is : ", filename
#print txt.read()

print "Type the name of your file : "
fileagn=raw_input("> ")

txtagn=open(fileagn)
print txtagn.read()
