#HelloAnybody.py;
#depencancies: HelloWorld
#last edit: 2020-05-13, by pWurster;
#desc:
#warm-up exercise for CSCI 111-900;

from HelloWorld import HelloWorld

class HelloAnybody(HelloWorld):

	def __init__(self, whomEver):
		super().__init__()
		self.content = f'{self.DEFAULT}, {whomEver}!'
