import numpy as np
import random
import math
import pickle

theta = math.atan(.2/.6)
#radius = .09 / math.sin(theta)
# radius lowered from .35 to .32
radius = .35
minDistance = 2*radius
# x from (b(0),b(1)), y from (b(2),b(3))
# possible points in [-1:0, -1:1]
b = [radius - 1.8, 1.8 - radius, radius - 1, 1 - radius]
xRange = (1.8 - radius) - (radius - 1.8)
yRange = (1 - radius) - (radius - 1)
# Number of possible iterations
numPos    = 10000
# Number of points per set
numPoints = 10
# Number of sets
numSets   = 100
# 300 x 2 x 10 x 1
genCoorVST = np.zeros([numSets,2,numPoints,1])

curSet = 0
np.random.seed()

while curSet < (numSets-1):  
    # Initialize random points
    x = np.random.random(numPos) * xRange + (radius - 1.8)
    y = np.random.random(numPos) * yRange + (radius - 1)

    # Initialize set
    keeperX = np.zeros([numPoints,1])
    keeperY = np.zeros([numPoints,1])

    # Initialize first point
    keeperX[0]  = x[0]
    keeperY[0]  = y[0]   
    # Number of points found 
    counter  = 1
    # Number of iterations
    iterator = 1
    while counter < (numPoints) and iterator < (numPos - 1):  
        thisX = x[iterator]
        thisY = y[iterator]

        distances = np.sqrt((thisX - keeperX)**2 + (thisY - keeperY)**2)
        minPointDistance = min(distances)
        if minPointDistance > minDistance:
            keeperX[counter] = thisX
            keeperY[counter] = thisY
            counter = counter + 1
        iterator += 1 
    if counter == (numPoints):  
        genCoorVST[curSet,0] = keeperX
        genCoorVST[curSet,1] = keeperY 
        curSet += 1  
        print(curSet)  

print(np.shape(genCoorVST))
print(genCoorVST[:][:][0][0])
print("done")
f = open('genCoorVST.pckl', 'wb')
pickle.dump(genCoorVST,f)
f.close()