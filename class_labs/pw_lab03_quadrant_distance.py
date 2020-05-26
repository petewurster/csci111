#pw_lab03_quadrant_distance.py;
#depencancies: math
#last edit: 2020-05-26, by pWurster;
#
#Gets x,y coords from the user, displays Cartesian Quadrant and distance
#from the origin in unspecified units to 3 points of precision
#

import math

#init variables
PRECISION: int = 3 #set precision for cleaner output
distance: float = 0.0 #units away from origin
point: list = [0, 0] #point at (x, y)
quadrant: str = 'I' #Cartesian quadrant I-IV (default is I)

#get input from user
print('Enter point values for (x, y)')
rawPoint = input('separated by a single SPACE: ')

#parse input into point as a list
point = list(map(lambda x: int(x), (rawPoint.split(' ')))) #just refreshing myself on 'map' syntax

#calculate hypotenuse to determint distance
distance = math.hypot(abs(point[0] - 0), abs(point[1] - 0))

#determine quadrant
if point[0] >= 0 and point[1] >= 0:
    pass
elif point[0] < 0 and point[1] >= 0:
    quadrant = 'II'
elif point[0] < 0 and point[1] < 0:
    quadrant = 'III'
else:
    quadrant = 'IV'

#display results
print(f'\nPoint ({point[0]}, {point[1]}) lies in Quadrant {quadrant} of the Cartesian plane')
print(f'and is {round(distance, PRECISION)} units away from the origin (0, 0).')
