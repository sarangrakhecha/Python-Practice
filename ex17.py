from sys import argv
from os.path import exists
script, infile,outfile = argv

#file1=infile.open()	#not allowed
file1=open(infile)
indata=file1.read()

print "Length of file1 is %d" %len(indata)

print "Does the output file exist? %r" % exists(outfile)
print "To abort, press ctrl-C"
print "else, hit return"
raw_input("? ");

file2=open(outfile,'w')
file2.write(indata)
#file2=write(indata)  #not allowed

file1.close()
file2.close();


