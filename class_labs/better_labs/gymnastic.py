#gymnastic.py;
#depencancies: none;
#last edit: 2020-05-23, by pWurster;
#get scores from 6 gymnastics judges & average them using a program modularized
#into functions with 'good' documentation (even though decent semantic naming
#practices can eliminate the need for most comments)

#func gets score from each judge & returns it as a float rounded to 1 place
def getScoreFrom(judge: str):
	return round(float(input(f'How do you score it {judge}? ')), 1)

#func calculates average of the collected scores & returns a float rounded to 2 places
def calculateAverageFrom(scores: dict):
	return round(sum(scores.values()) / len(scores), 2)

#func to display results
def display(results: str):
	print(results)

#this func controls the flow
def main():
	#this is the ONLY line in this prog that ACTUALLY warrants a comment
	#because it does several things in one line
	#create dictionary, setting scores to 0 for Judges 1-6 by zipping arrays
	judgeScores: dict = dict(zip(['Judge ' + str(x + 1) for x in range(6)], [0] * 6))
	
	#loop thru judges to assign their ratings
	for judge in sorted(judgeScores.keys()):
		judgeScores[judge] = getScoreFrom(judge)

	# display the results
	display(f'Average score is: {calculateAverageFrom(judgeScores)}')

#call the main function as long as this file wasn't imported as a module
if __name__ == '__main__': main()
