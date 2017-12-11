class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
		
	def sing_song(self):
		for line in self.lyrics:
			print line
			#print self.lyrics

song="asdsadfsdfasd"
happy_bday = Song(["Happy birthday to u",
				   "asdasdasd",
				   "asdasdasddfehrgh"])

trial=Song(["helloz"])

thanku = Song(["Thank u so much" "asdasdasd"])

happy_bday.sing_song()

thanku.sing_song()	

trial.sing_song()