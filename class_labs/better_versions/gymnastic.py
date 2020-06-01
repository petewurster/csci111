#gymnastic.py;
#depencancies: none;
#last edit: 2020-06-01, by pWurster;
#get scores from 6 gymnastics judges & average them using a program that is
#modularized into functions and is well documented

#init vars
NUMBER_OF_JUDGES: int = 6 #constant based on program requirement for 6 judges


#gets score from each judge & returns it as a float
def getScoreFrom(judge: str) -> float:
	return float(input(f'Score for {judge}: '))

#calculates average of the collected scores & returns a float
def calculateAverageFrom(scores: dict) -> float:
	return float(sum(scores.values()) / len(scores))

#use list comprehension and zip to create dictionary for tracking judge scores
def buildDictionaryToTrackJudgesScores(x: int) -> dict:
	return dict(zip(['Judge ' + str(y + 1) for y in range(x)], [0] * x))

#this func controls the flow
def main():
	#create dictionary, setting scores to 0 for Judges 1-6 by zipping arrays
	judgeScores: dict = buildDictionaryToTrackJudgesScores(NUMBER_OF_JUDGES)
	
	#loop thru judges to assign their ratings
	for judge in sorted(judgeScores.keys()):
		judgeScores[judge] = getScoreFrom(judge)

	#display the results
	print(f'The average score is: {calculateAverageFrom(judgeScores):.2f}')

#call the main function as long as this file wasn't imported as a module
if __name__ == '__main__': main()
