# Client Change-Detection Script
from VSTLoadImg import main
from trialGenerator import generate_experiment
import numpy as np
import pickle



# PARTICIPANT'S INITIALS
participant     = '001'

# WANT TO GET TO 8 AND 8
rectangleBlocks = 0
cubeBlocks      = 0
session         = 1






















################################ 
# DON'T WORRY ABOUT THIS STUFF #
################################

# PARAMETERS
stimType   = 1
blocks     = 2
tPerBlock  = 8
totalTrials = blocks * tPerBlock * 3


if rectangleBlocks == 0 & cubeBlocks == 0:
    trials = generate_experiment()
    with open(participant + 'VST','wb') as fp:
        pickle.dump(trials,fp)
with open(participant + 'VST','rb') as fp:
        trials = pickle.load(fp)
        


# TIMING
# each frame is 16.666667 ms
fCue       = 30  # 500 ms
fInterval  = 54  # 900 ms
fTest      = 120 # 2000 ms 
fPause     = 60  # 1000 ms 


# TRIAL SEQUENCING

# targChange: 0 if no change, 1 if change
# arraySize : 0 if min targets only, 1 if targets with distractors, 2 if max targets only

numTrials   = blocks*tPerBlock
blocksDone  = rectangleBlocks + cubeBlocks
arraySize   = []
targPresent = []
for j in range(blocksDone * numTrials, numTrials + blocksDone * numTrials):
    targPresent.append(trials[j][0])
    arraySize.append(trials[j][1])
    

print(len(trials))

print(targPresent)
print(arraySize)

#block = main(fCue,fInterval,fTest,fPause,tPerBlock,stimType,arraySize,targPresent,numTrials,participant,session)




