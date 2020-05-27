#HelloWorld.py;
#depencancies:none;
#last edit: 2020-05-13, by pWurster;
#desc:
#warm-up exercise for CSCI 111-900;

class HelloWorld:
	DEFAULT = 'Hello'

	def __init__(self):
		self.content = f'{HelloWorld.DEFAULT}, world!'

	def display(self):
		print(self.content)
