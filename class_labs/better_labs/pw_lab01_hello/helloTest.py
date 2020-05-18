#helloTest.py;
#depencancies: HelloAnybody, HelloWorld
#last edit: 2020-05-13, by pWurster;
#desc:
#warm-up exercise for CSCI 111-900;

from HelloAnybody import HelloAnybody, HelloWorld

def main():
	a = HelloWorld()
	a.display()

	b = HelloAnybody('prof Herbert')
	b.display()

	input('\n\n(press enter to quit)')

if __name__ == '__main__': main()
