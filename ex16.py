from sys import argv

script, filename=argv

print "We're gping to earse ", filename
print "Don't want, press ctrl-C"
print "else, hit return"

raw_input("?")

print "FIle opening"
target=open(filename,'w')

print"truncating the file"
print target.truncate()

print "Ask you for 3 lines"

line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
