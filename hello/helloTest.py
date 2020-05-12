#helloTest.py;
#dependancies: HelloWorld and HelloAnybody;
#warm-up exercise for CSCI 111-900;
#last edit: 12 May 2020 by pWurster;

from HelloAnybody import HelloAnybody, HelloWorld

def main():
	a = HelloWorld()
	a.display()

	b = HelloAnybody('prof Herbert')
	b.display()

	input('\n\n(press enter to quit)')

if __name__ == '__main__': main()
