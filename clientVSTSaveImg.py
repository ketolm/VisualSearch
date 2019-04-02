# Client Change-Detection Script
from VSTSaveImg import main
from trialGenerator import generate_trial, generate_block, generate_experiment
import pickle



# PARTICIPANT'S INITIALS
participant     = '001'

# WANT TO GET TO 8 AND 8
rectangleBlocks = 0
cubeBlocks      = 0





################################ 
# DON'T WORRY ABOUT THIS STUFF #
################################

# PARAMETERS
# targC     : 0 if no change,  1 if change
# stimType  : 0 if rectangles, 1 if cubes
# arrayS    : array size [2 4 6 8 10]
targP      = 1
stimType   = 1
arrayS     = 10



blocks     = 1
tPerBlock  = 200


# TIMING
# each frame is 16.666667 ms
fCue       = 1  # 200 ms
fStim      = 1  # 100 ms
fInterval  = 1  # 900 ms
fTest      = 1  # 2000 ms 
fPause     = 1  # 1000 ms 

# STIM SIZE
recLength  = .09
recWidth   = .27
cubeLength = .25
cubeWidth  = .25

# TRIAL SEQUENCING

# targChange: 0 if no change, 1 if change
# arraySize : 0 if min targets only, 1 if targets with distractors, 2 if max targets only

numTrials   = blocks*tPerBlock
blocksDone  = rectangleBlocks + cubeBlocks
arraySize   = []
targPresent = []
for j in range(200):
    targPresent.append(targP)
    arraySize.append(arrayS)

print(len(targPresent))



block = main(fCue,fStim,fInterval,fTest,fPause,recLength,recWidth,cubeLength,cubeWidth,tPerBlock,stimType,arraySize,targPresent,numTrials)




