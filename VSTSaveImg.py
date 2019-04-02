 ### Micah Ketola 
### Summer 2018
### CSNE Summer Program
### Saves VST images with different stimuli

from __future__ import absolute_import, division, print_function
from builtins import str
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.iohub import launchHubServer
from psychopy.visual import ShapeStim 
import random
import math
import pickle
import numpy
import time
import pylab
import os  # handy system and path functions
import sys  # to get file system encoding 
random.seed()

def main(fCue,fStim,fInterval,fTest,fPause,recLength,recWidth,cubeLength,cubeWidth,tPerBlock,stimType,arraySize,targPresent,numTrials):

    fStim       = fStim
    fTest       = fTest
    fPause      = fPause
    recLength   = recLength
    recWidth    = recWidth
    cubeLength  = cubeLength
    cubeWidth   = cubeWidth
    tPerBlock   = tPerBlock
    stimType    = stimType 
    arraySize   = arraySize
    targPresent = targPresent
    numTrials   = numTrials 
    
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir + u'\%s%s%s' %(targPresent[0],stimType,arraySize[0]))

    # Store info about the experiment session
    expName = 'VST.py'
    expInfo = {'session': '001', 'participant': ''}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    
    # 300 x 2 x 10 x 1 matrix 
    # 300 entries, xy for each shape, 10 shape locations
    f = open('genCoorVST.pckl', 'rb')
    genCoor = pickle.load(f)
    f.close()
    win = visual.Window([1600, 900], units = 'height', fullscr=True)
    clock = core.Clock()

    # KEYBOARD STUFF
    # Start iohub process. The iohub process can be accessed using `io`.
    io = launchHubServer()
    # A `keyboard` variable is used to access the iohub Keyboard device.
    keyboard = io.devices.keyboard
    events = keyboard.getKeys()
    
    # INITIALIZE
    # trialN       : number of trial
    # trialResp    : their response on each trial
    # correctResp  : if their response was correct
    # responseTime : the amount of time it took for them to respond on each trial
    m = 0
    trialN       = [-1 for x in range(numTrials)]
    trialResp    = [9 for x in range(numTrials)]
    correctResp  = [9 for x in range(numTrials)]
    responseTime = [0 for x in range(numTrials)]
    respChar     = [['r','i'],['f','j']]
    numSet       = 100
    rectangles = not stimType
    shapeN     = [[],[]]

    # COLORS
    recColors  = ['#0000ff','#ff0000']
    cubeColors = [['#0000ff','#9999ff','#000066'], ['#ff0000' ,'#ff9999','#660000']]
    
    # STIMULI
    center     = [0,0]
    posTheta   = [0, math.pi/4, math.pi/2, 3*math.pi/4]
    posCubes   = [0, 1] 
    pauseText  = visual.TextStim(win, text = "Press the Spacebar to Continue", font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb', opacity=1, depth=0.0)

    # rotates [x,y] by theta
    def rotate(xy,center,theta):
        #pts = {} Rotates points(nx2) about center by angle theta in radians
        return numpy.dot(xy-center,numpy.array([[math.cos(theta),math.sin(theta)],[-math.sin(theta),math.cos(theta)]]))+center
        
    def rotateRec(center,theta):
        center = center
        theta = theta
        p1 = [center[0]-recWidth, center[1]-recLength]
        p2 = [center[0]-recWidth, center[1]+recLength]
        p3 = [center[0]+recWidth, center[1]+recLength]
        p4 = [center[0]+recWidth, center[1]-recLength]
        rVert = rotate(numpy.array([p1, p2, p3, p4]),center,theta)
        return rVert

    # creates a three-sided cube
    def cubeCreator(centerV, cubeType):
        center = centerV
        cubeType = cubeType
        if cubeType == 0:
            p1 = [center[0]          , center[1]]
            p2 = [center[0]          , center[1]-cubeLength]
            p3 = [center[0]-cubeWidth, center[1]-cubeLength/2]
            p4 = [center[0]-cubeWidth, center[1]+cubeLength/2]
            sideOne = [p1, p2, p3, p4]
            
            q1 = [center[0]          , center[1]]
            q2 = [center[0]          , center[1]-cubeLength]
            q3 = [center[0]+cubeWidth, center[1]-cubeLength/2]
            q4 = [center[0]+cubeWidth, center[1]+cubeLength/2]
            sideTwo = [q1, q2, q3, q4]
            
            r1 = [center[0]          , center[1]]
            r2 = [center[0]-cubeWidth, center[1]+cubeLength/2]
            r3 = [center[0]          , center[1]+cubeLength]
            r4 = [center[0]+cubeWidth, center[1]+cubeLength/2]
            sideThree = [r1, r2, r3, r4]
        else:
            m1 = [center[0]          , center[1]]
            m2 = [center[0]          , center[1]+cubeLength]
            m3 = [center[0]+cubeWidth, center[1]+cubeLength/2]
            m4 = [center[0]+cubeWidth, center[1]-cubeLength/2]
            sideOne = [m1, m2, m3, m4]
            
            n1 = [center[0]          , center[1]]
            n2 = [center[0]          , center[1]+cubeLength]
            n3 = [center[0]-cubeWidth, center[1]+cubeLength/2]
            n4 = [center[0]-cubeWidth, center[1]-cubeLength/2]
            sideTwo = [n1, n2, n3, n4]
            
            s1 = [center[0]          , center[1]]
            s2 = [center[0]-cubeWidth, center[1]-cubeLength/2]
            s3 = [center[0]          , center[1]-cubeLength]
            s4 = [center[0]+cubeWidth, center[1]-cubeLength/2]
            sideThree = [s1, s2, s3, s4]
            # k cubes x 3 sides x 4 vertices x 2 coordinates
        cVert = [sideOne, sideTwo, sideThree]
        return cVert
        

    def randShuf(inputList):
        shufList = inputList[:]
        while True:
            random.shuffle(shufList)
            for a, b in zip(inputList, shufList):
                if a == b:
                    break
                else:
                    return shufList
                    
    def recDraw(frames, nStim, stimulus, changeT,order):
                frames = frames
                for k in range(nStim):
                    stimulus[k].draw()
                print('stimType%d_arraySize%d_trial%d_targPresent%d_order%d.png' % (stimType,arraySize[t],t,targPresent[t],order))
                time.sleep(0.03)
                win.getMovieFrame(buffer = 'back')
                win.flip()
                win.saveMovieFrames('stimType%d_arraySize%d_trial%d_targPresent%d_order%d.png' % (stimType,arraySize[t],t,targPresent[t],order))

    def cubeDraw(frames, nStim, stimulus,changeT,order):
                frames = frames
                for j in range(nStim):
                    for k in range(3):
                        stimulus[j][k].draw()
                        stimulus[j][k].draw()
                print('stimType%d_arraySize%d_trial%d_targPresent%d_order%d.png' % (stimType,arraySize[t],t,targPresent[t],order))
                time.sleep(0.03)
                win.getMovieFrame(buffer = 'back')
                win.flip()
                win.saveMovieFrames('stimType%d_arraySize%d_trial%d_targPresent%d_order%d.png' % (stimType,arraySize[t],t,targPresent[t],order))

    for t in range(numTrials):
        if (t % tPerBlock == 0) & (t > 1):
            waiting = []
            while not ' ' in waiting:
                pauseText.draw()
                win.flip()
                waiting = keyboard.getKeys()
        random.shuffle(recColors[0][0])
        trialN[t] = t + 1
        nStim    = arraySize[t]
        shapes   = [[] for i in range(nStim)]
        recStim  = [[] for i in range(nStim)]
        recVert  = [[] for i in range(nStim)]
        cubeV    = [[] for i in range(nStim)]
        # 3 because 3 sides
        targCube = [[] for i in range(3)]
        cubeStim = [[[],[],[]] for i in range(nStim)]
        stimIndex = nStim - 1

        # START WORKING HERE
        # Choose random trial and get center coordinates of objects
        # ASSUMING ARRAYSIZE[T] IS A VECTOR OF ARRAY SIZES
        # genCoor (300 x 2 x 10 x 1)
        #          300 sets, (X pos, Y pos), 10 points
        # x any y pos of arraySize[t] locations
        randInt = random.randint(0,numSet-1)
        for j in range(0, nStim):
            xCoor = genCoor[randInt,0,j]
            yCoor = genCoor[randInt,1,j]
            shapes[j] = [xCoor[0], yCoor[0]]


        if rectangles:
            # create a unique rectangle that will only been seen once or not at all
            random.shuffle(posTheta)
            coinFlip     = (random.random() > .5)
            targTheta    = posTheta[0]
            targColor    = coinFlip
            targRectVert = rotateRec([0,0],targTheta)
            
            # creates unique rectangle for cue
            targRect = ShapeStim(win, vertices = targRectVert, fillColor = recColors[targColor], size = .5)
            
            # creates numRect rectangles with random orientations and random colors
            for k in range(nStim):
                coinFlip = (random.random() > .5)
                random.shuffle(posTheta)
                while posTheta[0] == targTheta and coinFlip == targColor:
                    coinFlip = (random.random() > .5)
                    random.shuffle(posTheta)
                recVert[k] = rotateRec(shapes[k],posTheta[0])
                recStim[k] = ShapeStim(win, vertices = recVert[k], fillColor = recColors[coinFlip], size = .5)
                coinFlip = (random.random() > .5)
                random.shuffle(posTheta)
                
        else:
            # create a unique cube that will only been seen once or not at all
            random.shuffle(posCubes)
            coinFlip        = (random.random() > .5)
            targOrientation = posCubes[coinFlip]
            random.shuffle(cubeColors[coinFlip])
            targCubeColors  = cubeColors[coinFlip][:]
            targCubeVert    = cubeCreator([0,0],targOrientation)
            
            # creates unique cube for cue
            for b in range(3):
                targCube[b] = ShapeStim(win, vertices = targCubeVert[b], fillColor = targCubeColors[b], size = .5)

            for j in range(nStim):
                coinFlip = (random.random() > .5)
                random.shuffle(posCubes)
                random.shuffle(cubeColors[0])
                random.shuffle(cubeColors[1])
                while posCubes[0] == targOrientation and cubeColors[coinFlip] == targCubeColors:
                    coinFlip = (random.random() > .5)
                    random.shuffle(posCubes)
                    random.shuffle(cubeColors[0])
                    random.shuffle(cubeColors[1])

                cubeVert = cubeCreator(shapes[j],posCubes[0])
                cubeV[j] = cubeCreator(shapes[j],posCubes[0])
                
                # creates each side
                for i in range(3):
                    cubeStim[j][i] = ShapeStim(win, vertices = cubeVert[i], fillColor = cubeColors[coinFlip][i], size = .5)



        # STIM PRESENTATION
        
        #
        # presents target
        if rectangles:
            recDraw(fStim, 1, [targRect], targPresent[t],0)
        else:
            cubeDraw(fStim, 1, [targCube], targPresent[t],0)

        ## presents interval
        #for frameN in range(fPause + 1):
        #    win.flip()

        # presents stim
        if targPresent[t]:
            if rectangles:
                # inserts target rectangle into line-up
                targRect = rotateRec(shapes[0],targTheta)
                recStim[0] = ShapeStim(win, vertices = targRect, fillColor = recColors[targColor], size = .5)
                
                recDraw(fStim, nStim, recStim, targPresent[t],1)
            else:
                # inserts target cube into line-up
                for b in range(3):
                    cubeStim[0][b] = ShapeStim(win, vertices = cubeV[0][b], fillColor = targCubeColors[b], size = .5)
                
                cubeDraw(fStim, nStim, cubeStim, targPresent[t],1)
        else:
            if rectangles:
                recDraw(fStim,  nStim, recStim, targPresent[t],1)
            else:
                cubeDraw(fStim, nStim, cubeStim, targPresent[t],1)
        
        
        if trialResp[t] == targPresent[t]:
            correctResp[t] = 1
        else:
            correctResp[t] = 0

    # OUTPUT
    print()
    print('Correct response trials')
    print(correctResp)
    print('Percent correct')
    print(sum(correctResp) / numTrials)
    print('Response Time')
    print(responseTime)
    print('Average response time')
    print(sum(responseTime) / numTrials)
    
    
    thisExp.addData('correct responses',correctResp)
    thisExp.nextEntry()
    thisExp.addData('response times', responseTime)
    thisExp.nextEntry()
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    
    origLUT = numpy.round(win.backend._origGammaRamp * 65535.0).astype("uint16")
    origLUT = origLUT.byteswap() / 255.0
    win.backend._origGammaRamp = origLUT
    
    win.close()
    core.quit()