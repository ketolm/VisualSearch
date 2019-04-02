 ### Micah Ketola 
### Summer 2018
### CSNE Summer Program
### Saves VST images with different stimuli

from __future__ import absolute_import, division, print_function
from builtins import str
from psychopy import data, logging, visual, sound, core, event, clock
from psychopy.visual import ShapeStim 
import time
import random
import math
import pickle
import numpy
import pylab
import os  # handy system and path functions
import sys  # to get file system encoding
random.seed()

def main(fCue,fInterval,fTest,fPause,tPerBlock,stimType,arraySize,targPresent,numTrials,participant,session):
    
    fCue        = fCue
    fInterval   = fInterval
    fTest       = fTest
    fPause      = fPause
    tPerBlock   = tPerBlock
    stimType    = stimType 
    arraySize   = arraySize
    targPresent = targPresent
    numTrials   = numTrials 
    
    _thisDir = "C:/Users/micah/Documents/Honors Project/Visual Search Task/"
    
    # Store info about the experiment session
    expName = 'Visual Search Task.py'
    expInfo = {'session': session, 'participant': participant}
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    thisExp = data.ExperimentHandler(name=expName,
                    version='0.1',
                    extraInfo={'participant': participant},
                    runtimeInfo=None,
                    originPath=None,
                    savePickle=True,
                    saveWideText=True,
                    dataFileName=filename)
    
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    
    win = visual.Window([1600, 900], units = 'height', fullscr=True)
    clock = core.Clock()

    # KEYBOARD STUFF 
    # iohub is broken currently 
    events = event.getKeys()
    
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
    
    pauseText  = visual.TextStim(win, text = "Press the Spacebar to Continue", font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb', opacity=1, depth=0.0)

    for t in range(numTrials):
        trialTime = time.time()
        if (t % tPerBlock == 0) & (t > 1):
            event.clearEvents(eventType='keyboard')
            waiting = []
            tStart = time.time()
            while not 'space' in waiting:
                waiting = event.getKeys(keyList=['space'])
                pauseText.draw()
                win.flip()
            pauseTime = time.time() - tStart
            thisExp.addData('pauseTime', pauseTime)
        
        trialN[t] = t + 1
        
        # STIM PRESENTATION
        randTrial = random.randint(1,100)
        cueName   = 'stimType%d_arraySize%d_targPresent%d_order%d (%d).png' % (stimType, arraySize[t], targPresent[t], 0, randTrial)
        cueDir    = '%d%d%d/' % (targPresent[t], stimType, arraySize[t]) + cueName
        cueStim   = visual.ImageStim(win, image = cueDir)

        stimName  = 'stimType%d_arraySize%d_targPresent%d_order%d (%d).png' % (stimType, arraySize[t], targPresent[t], 1, randTrial)
        stimDir   = '%d%d%d/' % (targPresent[t], stimType, arraySize[t]) + stimName
        arrayStim = visual.ImageStim(win, image = stimDir)
        
        # presents array
        for frameN in range(fCue + 1):
            cueStim.draw()
            win.flip()
        
        for frameN in range(fInterval + 1):
            win.flip()
            
        startT = time.time()
        for frameN in range(fTest + 1):
            theseKeys = event.getKeys(keyList=['f','j'])
            if len(theseKeys) > 0:  # at least one key was pressed
                trialResp[t]    = theseKeys[-1]  # just the last key pressed
                responseTime[t] = time.time() - startT
            arrayStim.draw()
            win.flip()
            
        for frameN in range(fPause + 1):
            win.flip()
        
        # f means no target, j means yes target
        if targPresent[t]:
            correctResp[t] = trialResp[t] == 'j'
        else:
            correctResp[t] = trialResp[t] == 'f'

        # OUTPUT
        thisExp.addData('stimType', stimType)
        thisExp.addData('arraySize', arraySize[t])
        thisExp.addData('targPresent', targPresent[t])
        thisExp.addData('startTime', trialTime)
        thisExp.addData('responseTime', responseTime[t])
        thisExp.addData('trialKeyPress', trialResp[t])
        thisExp.addData('correctResponse',correctResp[t])
        thisExp.addData('trialNumber', trialN[t])
        thisExp.addData('stimulusHandle', stimName)
        thisExp.nextEntry()
        
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()
        
            
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()