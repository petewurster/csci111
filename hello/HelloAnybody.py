#HelloAnybody.py;
#dependancies: HelloWorld;
#warm-up exercise for CSCI 111-900;
#last edit: 11 May 2020 by pWurster;

from HelloWorld import HelloWorld

class HelloAnybody(HelloWorld):

	def __init__(self, whomEver):
		super().__init__()
		self.content = f'{self.DEFAULT}, {whomEver}!'
