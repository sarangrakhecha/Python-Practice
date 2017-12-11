from sys import exit

def gold_room():
	print"Full gold. How much?"
	
	next=raw_input("> ")
	#if "0" in next or "1" in next:		#even writing this syntax is correct
	if next=="0" or next == "1":
		how_much=int(next)
	else:
		dead("Type a number !!")
		
	if how_much<50:
		print"Not greedy"
		exit(0)
	else:
		dead("Greeady!!!!!!!!!!")
		
def bear_room():
	print"bear\nhoney\nmove the bear!!\n"
	bear_moved=False
	while True:
		next=raw_input("> ")
		if next == "take honey":
			dead("slaps")
		elif next=="taunt bear" and not bear_moved:
			print "Bear move.u may go"
			bear_moved=True
		elif next=="taunt bear" and bear_moved:
			dead("Bear pissed!")
		elif next=="open door" and bear_moved:
			gold_room()
		else:
			print "No idea what it means!!"

def bear1_room():
	print"great eveil bear"
	next = raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Tasty food!")
	else:
		bear1_room()

def dead(why):
	print why, "good job"
	exit(0)

def start():
	print"in dark room"
	next=raw_input("> ")
	if next=="left":
		bear_room()
	elif next=="right":
		bear1_room()
	else:
		dead("Stumble around the room")
		
start()
	