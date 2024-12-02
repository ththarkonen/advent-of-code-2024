import numpy as np

def parse( lines ):

    data = []

    for line in lines:

        line = line.split(" ")
        row = np.fromiter( line, dtype = int)

        data.append( row )

    return data


def levelSafety( level ):

    levelChanges = np.diff( level )
    absoluteChanges = np.abs( levelChanges )

    decreasing = np.all( levelChanges < 0 )
    increasing = np.all( levelChanges > 0 )
    slowEnough = np.all( absoluteChanges <= 3 )

    safety = np.logical_xor( decreasing, increasing)
    safety = np.logical_and( safety, slowEnough)

    return safety


def makeDampenedLevel( level, dampenIndex):

    nSteps = len( level )

    if dampenIndex == nSteps:
        dampenedLevel = level
    else:
        dampenedLevel = np.delete( level, dampenIndex)

    return dampenedLevel


def analyzeSafety( data ):

    safeLevels = []

    for level in data:

        safeLevel = levelSafety( level )
        safeLevels.append( safeLevel )

    return safeLevels


def analyzeDampenedSafety( data ):

    safeLevels = []

    for level in data:

        nSteps = len( level )
        safeLevel = False

        for ii in range( nSteps + 1 ):
            
            dampenedLevel = makeDampenedLevel( level, dampenIndex = ii)
            safeLevel = levelSafety( dampenedLevel )

            if safeLevel:
                break

        safeLevels.append( safeLevel )

    return safeLevels

