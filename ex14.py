from sys import argv

script, uname=argv

prompt = "--> "

print "Hi %s I'm the %s script" %(uname,script)
print"few questions"
print"do u like me %s" %uname
likes=raw_input(prompt)

print"where do u live ", uname
live=raw_input(prompt)


print"""
u said %r about liking me.
u live in %r
""" %(likes,live)
