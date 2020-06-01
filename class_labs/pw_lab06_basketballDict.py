#pw_lab06_basketballDict.py;
#depencancies: none;
#last edit: 2020-06-01, by pWurster;
#demonstrate basic dictionary functions via assignment, iteration,
#and dict[key] access to display some sports results

#init vars
playerPoints: dict = dict(Bolden = 1, Butler = 11, Embiid = 31, Ennis = 7, Harris = 24,
                          Marjanovic = 4, McConnell = 2, Reddick = 9, Scott = 8, Simmons = 15)
highestScoringPlayer:str = '' #init to empty string
highScore:int = 0 #will be set in loop
totalScore: int = 0 #accumulator

#loop over player/points dictionary
for player in playerPoints:
    totalScore += playerPoints[player] #update accumulator

    #update high score as needed
    if playerPoints[player] > highScore:
        highScore = playerPoints[player]
        highestScoringPlayer = player

    #display each player's points
    print(f'{player} scored {playerPoints[player]} points.')

#display final tally
print(f'\nCombined total of {totalScore} points, {highestScoringPlayer} had the most points.')
