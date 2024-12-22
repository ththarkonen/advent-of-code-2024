
import numpy as np

moves = ( np.array([-1, 0]), np.array([ 0, 1]),
          np.array([ 1, 0]), np.array([ 0,-1]) )

def parse( lines ):

    bytes = []

    for line in lines:

        xy = line.split(",")
        xy = [ int(d) for d in xy ]
        bytes.append( xy )

    return bytes


def updateState( p, move):

    ii = p[0]
    jj = p[1]
    score = p[2
              ]
    nextState = ( ii + int(move[0]), jj + int(move[1]), score + 1)
    return nextState


def checkState( state, maze, scores):

    nRows, nCols = maze.shape

    ii = state[0]
    jj = state[1]
    key = state[0:2]
    score = state[2]

    if ii < 0 or ii >= nRows: return False
    if jj < 0 or jj >= nCols: return False
    if maze[ ii, jj] == -1: return False
    if key in scores and score >= scores[ key ]: return False

    scores[ key ] = score

    return True


def dodge( bytes, limits, time):

    nRows, nCols = limits
    start = ( 0, 0, 0)
    stop = ( nRows - 1, nCols - 1)

    statesNext = [ start ]

    scores = {}
    scores[ start[0:2] ] = 0

    memoryMap = np.zeros( limits )

    for ii in range( time ):
        memoryMap[ bytes[ii][0], bytes[ii][1]] = -1

    while True:

        states = statesNext.copy()
        statesNext = []

        for state in states:
             for move in moves:
                  
                nextState = updateState( state, move)
                validState = checkState( nextState, memoryMap, scores)

                if not validState: continue

                statesNext.append( nextState )

                if nextState[0:2] == stop:
                    return nextState

        noNewStates = len( statesNext ) == 0
        if noNewStates: break

    return []


def getLastPath( bytes, memoryLimits, startTime):

    nBytes = len( bytes ) 

    for t in range( startTime, nBytes):

        path = dodge( bytes, memoryLimits, t)
        if len( path ) == 0: break

        print( t / nBytes )

    ind = t - 1
    return bytes[ ind ]