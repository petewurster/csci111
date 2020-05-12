#helloTest.py;
#dependancies: HelloWorld and HelloAnybody;
#warm-up exercise for CSCI 111-900;
#last edit: 11 May 2020 by pWurster;

from HelloAnybody import HelloAnybody, HelloWorld

def main():
	a = HelloWorld()
	a.display()

	b = HelloAnybody('prof Herbert')
	b.display()


main()
