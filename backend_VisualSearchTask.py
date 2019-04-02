### Micah Ketola 
### Autumn 2018
### Psychology Honors Project
### Visual Search Task with different stimuli


from __future__ import absolute_import, division, print_function
from builtins import str
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.iohub import launchHubServer
from psychopy.visual import ShapeStim 
import time
import random
import math
import pickle
import numpy
import pylab
import os  # handy system and path functions
import sys  # to get file system encoding

def main(fCue,fStim,fInterval,fTest,fPause,tPerBlock,stimType,targPresent,arraySize,numTrials,blocks):
    
    fCue         = fCue
    fStim        = fStim
    fTest        = fTest
    fPause       = fPause
    tPerBlock    = tPerBlock
    stimType     = stimType 
    trialPresent = trialPresent
    arraySize    = arraySize
    numTrials    = numTrials
    
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)

    # Store info about the experiment session
    expName = 'VisualSearchTask.py'
    expInfo = {'session': '001', 'participant': ''}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date']    = data.getDateStr()  # add a simple timestamp
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

    win = visual.Window(size = [1600, 900], units = 'height', fullscr=True)

    # STIMULI
    pauseText  = visual.TextStim(win, text = "Press the Spacebar to Continue", font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb', opacity=1, depth=0.0)

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
    pauseTime    = [0 for x in range(blocks)]
    respChar     = [['r','i'],['f','j']]
    
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
        stimName  = 'stimType%d_trialType%d_cue%d_order%d (%d).png' % (stimType, trialType[t], 0, randTrial)
        stimDir      = '%d%d%d/' % (stimType, arraySize[t]) + stimName
        
        
        # STIM PRESENTATION
        randTrial = random.randint(1,100)
        stimName  = 'stimType%d_trialType%d_cue%d_order%d (%d).png' % (stimType, trialType[t], cue[t], 0, randTrial)
        stimDir      = '%d%d%d/' % (stimType, trialType[t], cue[t]) + stimName
        
        # presents cue
        for frameN in range(fCue + 1):
            fixation.draw()
            fixation2.draw()
            if cue[t]:
                arrowRight.draw()
            else:
                arrowLeft.draw()
            win.flip()
        
        # presents stim
        for frameN in range(fStim + 1):
            stim = visual.ImageStim(win, image = stimDir)
            stim.draw()
            win.flip()
            
        
        # presents interval
        for frameN in range(fInterval + 1):
            fixation.draw()
            fixation2.draw()
            win.flip()

        # presents test array
        if targChange[t]:
            stimName  = 'stimType%d_trialType%d_cue%d_order%d (%d).png' % (stimType, trialType[t], cue[t], 1, randTrial)
            stimDir   = '%d%d%d/' % (stimType, trialType[t], cue[t]) + stimName
            stim      = visual.ImageStim(win, image = stimDir)
            
        startT = time.time()
        for frameN in range(fTest + 1):
            theseKeys = event.getKeys(keyList=['r', 'f', 'i', 'j'])
            if len(theseKeys) > 0:  # at least one key was pressed
                trialResp[t]    = theseKeys[-1]  # just the last key pressed
                responseTime[t] = time.time() - startT
            stim.draw()
            win.flip()
            
        # presents interval
        for frameN in range(fPause + 1):
            fixation.draw()
            fixation2.draw()
            win.flip()
        
        if cue[t]:
            if targChange[t]:
                if trialResp[t] == 'i':
                    correctResp[t] = 1
                else:
                    correctResp[t] = 0
            else:
                if trialResp[t] == 'j':
                    correctResp[t] = 1
                else:
                    correctResp[t] = 0
        else:
            if targChange[t]:
                if trialResp[t] == 'r':
                    correctResp[t] = 1
                else:
                    correctResp[t] = 0
            else:
                if trialResp[t] == 'f':
                    correctResp[t] = 1
                else:
                    correctResp[t] = 0
                    
        # OUTPUT 
        thisExp.addData('stimType', stimType)
        thisExp.addData('trialType', trialType[t])
        thisExp.addData('targChange', targChange[t])
        thisExp.addData('cue', cue[t])
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
    origLUT = numpy.round(win.backend._origGammaRamp * 65535.0).astype("uint16")
    origLUT = origLUT.byteswap() / 255.0
    win.backend._origGammaRamp = origLUT
    win.close()
    core.quit()
        
        
        