import numpy as np

moveTypes = ("move", "turnLeft", "turnRight")

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    maze = np.zeros( dims )

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):

            if c == "#":
                maze[ ii, jj] = -1
            if c == "S":
                start = ( ii, jj, 0, 1, 0)
            if c == "E":
                stop = ( ii, jj)

    return maze, start, stop


def checState( state, maze, scores):

    nRows, nCols = maze.shape

    ii = state[0]
    jj = state[1]
    key = state[0:4]
    score = state[4]

    if ii < 0 or ii >= nRows: return False
    if jj < 0 or jj >= nCols: return False
    if maze[ ii, jj] == -1: return False
    if key in scores and score > scores[key]: return False

    scores[key] = score

    return True


def updateState( p, moveType):

    ii = p[0]
    jj = p[1]

    vi = p[2]
    vj = p[3]

    score = p[4]

    if moveType == "move":

        nextII = ii + vi
        nextJJ = jj + vj

        score += 1
        nextState = ( nextII, nextJJ, vi, vj, score)
        
    elif moveType == "turnLeft":

            score += 1000
            nextDirectionScore = ( vj, -vi, score)

            nextState = ( ii, jj) + nextDirectionScore
 
    elif moveType == "turnRight":

            score += 1000
            nextDirectionScore = ( -vj, vi, score)

            nextState = ( ii, jj) + nextDirectionScore

    return nextState


def travel( maze, start, stop):

    statesNext = [ [start] ]
    startKey = start[0:4]

    scores = {}
    scores[ startKey ] = 0

    stopStates = []

    while True:

        states = statesNext.copy()
        statesNext = []

        for state in states:
             for moveType in moveTypes:

                if state[-1][0:2] == stop:

                    stopStates.append( state.copy() )
                    continue
                  
                nextState = updateState( state[-1], moveType)
                validState = checState( nextState, maze, scores)

                if not validState: continue

                nextPath = state.copy()
                nextPath.append( nextState )
                statesNext.append( nextPath )

        noNewStates = len( statesNext ) == 0
        if noNewStates: break

    return scores, stopStates


def getTopScore( scores, stop):
     
    stopStates = [ stop + ( 0, 1),
                   stop + ( 1, 0),
                   stop + (-1, 0),
                   stop + ( 0,-1)]
     
    stopScores = []

    for stopState in stopStates:
        if stopState not in scores: continue
        
        stopScores.append( scores[ stopState ] )

    return min( stopScores )


def getSeats( paths, stop, topScore):

    seats = set()
     
    stopStates = [ stop + ( 0, 1, topScore),
                   stop + ( 1, 0, topScore),
                   stop + (-1, 0, topScore),
                   stop + ( 0,-1, topScore)]

    for path in paths:
        for stopState in stopStates:
            if stopState not in path: continue

            for state in path:
                location = ( state[0], state[1])
                seats.add( location )

    return seats

                  

