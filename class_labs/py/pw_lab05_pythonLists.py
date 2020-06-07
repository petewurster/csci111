#pw_lab05_pythonLists.py;
#depencancies: random
#last edit: 2020-06-01, by pWurster;
#demonstrate looping methods via building a list full of random numbers
#and then finding sum, min, max, and avg of the values in the list

import random

#init vars
MAX_LIST_LENGTH = 1000      #must be set > 0
numberList: list = []       #empty list
sumOfNumberList: int = 0    #init the accumulator
smallestNumber: int         #set after list is built
largestNumber: int          #set after list is built

count = 0 #temp var
#fill list via count-controlled while loop
while count < MAX_LIST_LENGTH:
    numberList.append(random.randrange(1, 101))
    count += 1

#set vars to 1st val in list
smallestNumber = numberList[0] #could also use arbitrary high val like float('Inf')
largestNumber = numberList[0] #could also use arbitrary low val like float('-Inf')

#process list via for loop
for currentNumber in numberList:
    #update accumulator
    sumOfNumberList += currentNumber
    #set new min as appropriate
    if currentNumber < smallestNumber: smallestNumber = currentNumber
    #set new max as appropriate
    if currentNumber > largestNumber: largestNumber = currentNumber

#display results
print(f'sum: {sumOfNumberList}\tmin: {smallestNumber}\tmax: {largestNumber}\tavg: {sumOfNumberList / len(numberList)}')
