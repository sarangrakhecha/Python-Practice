from sys import argv
script,input_file=argv

def print_all(f):
	print f.read()
	
def print_rewind(f):
	f.seek(0)
	
def print_current(line_count,f):
	print line_count, f.readline()

current_file=open(input_file)

print"read file\n"

print_all(current_file)

print("\nRewind it")
print_rewind(current_file)

print"\nprint lines"

curr_line=1
print_current(curr_line,current_file)

curr_line=curr_line+1
print_current(curr_line,current_file)

curr_line=curr_line+1
print_current(curr_line,current_file)