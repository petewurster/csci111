#HelloWorld.py;
#warm-up exercise for CSCI 111-900;
#last edit: 11 May 2020 by pWurster;

class HelloWorld:
	DEFAULT = 'Hello'

	def __init__(self):
		self.content = f'{HelloWorld.DEFAULT}, world!'

	def display(self):
		print(self.content)
