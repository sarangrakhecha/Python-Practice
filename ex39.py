states = {
	'Oregon': 'OR',
	'NewYork':'NY',
	'Florida':'FL'
}

cities = {'FL':'Miami',
		  'NY':'Binghamton'
		 }
			
cities['NJ'] = 'Jersey City'
cities['CA'] = 'Mountain View'

b=cities.get("FL",None)

print "\n"
print "*"*100
print "\n"
print "NY state has : ",cities['NY']
print "FL state has : ",cities['FL']

print "*"*100
print "Newyork's abbr is : ",states['NewYork']
print "Florida's abbr is : ",states['Florida']

print "*"*100
#state and city
print "Florida has : ",cities[states['Florida']]


print "*"*100
for state, abbr in states.items():
	print "%s is abbr of %s" %(abbr,state)
	
for abbr,city in cities.items():
	print "%s belongs to state %s" %(city,abbr)
	
for state, abbr in states.items():
	print "%s state1 is abbreviated %s and has city %s" %(state,abbr,cities.get(abbr,None))	
	
state=states.get('Texas',None)

if not state:
	print "Sorry, no texas"
	
city=cities.get('TX','Does not exist')
print "The city for state TX is : %s" %city

	
#for state,abbr in states.items():						##IN THE BOOK...NOT WORKING. hENCE TRIED THE ABOVE SYNTAX(LINE 38,39)
	#print "%s state2 is abbreviated %s and has city %s" %(state,abbr,cities[abbr])	