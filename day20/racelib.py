import numpy as np
from collections import Counter

moves = ( np.array([-1, 0]), np.array([ 0, 1]),
          np.array([ 1, 0]), np.array([ 0,-1]) )

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    racemap = np.zeros( dims )

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):
            
            if c == "#":
                racemap[ ii, jj] = -1
            if c == "S":
                start = ( ii, jj)
            if c == "E":
                stop = ( ii, jj)

    return start, stop, racemap


def updateState( p, move):

    ii = p[0]
    jj = p[1]
    score = p[2]
    
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


def tracePath( start, stop, racemap):

    statesNext = [ start + tuple([0]) ]

    scores = {}
    scores[ start[0:2] ] = 0
    path = {}

    while True:

        states = statesNext.copy()
        statesNext = []

        for state in states:
             for move in moves:
                  
                nextState = updateState( state, move)
                validState = checkState( nextState, racemap, scores)

                if not validState: continue
                statesNext.append( nextState )
                path[( state[0], state[1])] = state[-1]

                if nextState[0:2] == stop:  
                    path[( nextState[0], nextState[1])] = nextState[-1]
                    return path
                
        noNewStates = len( statesNext ) == 0
        if noNewStates: break

    return []


def getPathInRadius( p, pathInds, radius):

    ii = p[0]
    jj = p[1]

    validInds = []
    distances = []

    for inds in pathInds:
        if p == inds: continue

        pathII = inds[0]
        pathJJ = inds[1]

        l1 = np.abs( pathII - ii ) + np.abs( pathJJ - jj )
        
        if l1 <= radius:

            pathLocation = ( pathII, pathJJ)

            validInds.append( pathLocation )
            distances.append( l1 )

    return validInds, distances


def computeSpeedups( p, validInds, distances, path, stop, minimumSpeedup):

    speedUps = []

    for counter, inds in enumerate( validInds ):
        d = distances[ counter ]
        speedup = ( path[ stop ] - path[ inds ] ) + int( d ) + path[ p ]
        speedup = path[stop] - int( speedup )

        if speedup >= minimumSpeedup:
            speedUps.append( speedup )

    return speedUps


def cheat( path, stop, radius, minimumSpeedup):

    speedUps = []

    for ii, p in enumerate( path ):

        validInds, distances = getPathInRadius( p, path, radius)
        validSpeedups = computeSpeedups( p, validInds, distances, path, stop, minimumSpeedup)

        speedUps += validSpeedups
        print( ii / path[stop] )

    return Counter( speedUps )