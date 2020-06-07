#gymnastic.py;
#depencancies: none;
#last edit: 2020-06-01, by pWurster;
#get scores from 6 gymnastics judges & average them using a program that is
#modularized into functions and is well documented

#constant based on program requirement for 6 judges
NUMBER_OF_JUDGES: int = 6

#gets score from each judge & returns it as a float
def getScoreFrom(judge: int) -> float:
    return float(input(f'Score for Judge {judge + 1}: '))


#calculates avg of collected scores & returns avg as a float
def calculateAverageFrom(totalScore: float) -> float:
    return float(totalScore / NUMBER_OF_JUDGES)


#controls program flow
def main():
    totalScore: float = 0.0 #init accumulator
    #loop thru judges to assign their ratings
    for judge in range(0, NUMBER_OF_JUDGES):
        totalScore += getScoreFrom(judge)   #update accumulator

    #display the results
    print(f'The average score is: {calculateAverageFrom(totalScore):.2f}')


#call main function as long as this file wasn't imported as a module
if __name__ == '__main__': main()
