import numpy as np
from joblib import Parallel, delayed

R = np.array([[ 0, 1],
              [-1, 0]])

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    map = np.full( dims, False)

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):

            if c == "^":
                guard = {}
                guard["position"] = ( ii, jj)
                guard["direction"] = np.array([ -1, 0])

            if c == "#":
                map[ ii, jj] = True

    return guard, map


def simulate( guard, map):

    nRows, nCols = map.shape
    positions = [ guard["position"] ]

    while True:

        ii = guard["position"][0]
        jj = guard["position"][1]

        v = guard["direction"]

        nextII = ii + v[0]
        nextJJ = jj + v[1]
        nextPosition = ( nextII, nextJJ)

        if nextII < 0 or nextII >= nRows: break
        if nextJJ < 0 or nextJJ >= nCols: break

        isObstacle = map[ nextII, nextJJ]

        if isObstacle:
            guard["direction"] = R @ guard["direction"]
            continue

        guard["position"] = nextPosition

        if nextPosition not in positions:
            positions.append( nextPosition )

    return positions


def loopChecker( guard, map):

    nRows, nCols = map.shape
    loop = False

    nextState = guard["position"] + tuple( guard["direction"] ) 
    states = [ nextState ]

    while True:

        state = nextState

        ii = state[0]
        jj = state[1]

        v = state[2]
        w = state[3]

        nextII = ii + v
        nextJJ = jj + w

        if nextII < 0 or nextII >= nRows: break
        if nextJJ < 0 or nextJJ >= nCols: break

        isObstacle = map[ nextII, nextJJ]

        if isObstacle:

            x = state[2]
            y = state[3]

            nextDirection = ( y, -x)
            nextState = ( ii, jj) + nextDirection
        else:

            nextPosition = ( nextII, nextJJ)
            nextState = nextPosition + ( v, w)

        if nextState in states: loop = True
        if loop: break

        states.append( nextState )

    return loop


def parallelCallback( p, guard, map):

    ii = p[0]
    jj = p[1]
    
    map[ ii, jj] = True
    blockLocation = ( ii, jj)

    if blockLocation == guard["position"]:

        block = {}
        block["loop"] = False
        block["location"] = blockLocation

        return block

    looped = loopChecker( guard, map)

    block = {}
    block["loop"] = looped
    block["location"] = blockLocation

    return block


def getLoopingBlocks( positions, guard, map):

    nJobs = 24

    parfor = Parallel( n_jobs = nJobs )
    call = delayed( parallelCallback )

    nLocations = len( positions )
    inds = range( nLocations )

    lambdaCall = lambda ii : call( positions[ii], guard, map.copy())
    blocks = parfor( lambdaCall(ii) for ii in inds)

    blockLocations = [ block["location"] for block in blocks if block["loop"] ]
    return blockLocations