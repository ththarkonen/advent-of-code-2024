import numpy as np

moves = ( np.array([-1, 0]), np.array([ 0, 1]),
          np.array([ 1, 0]), np.array([ 0,-1]) )

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    map = np.zeros( dims )

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):
            if c == "\n": continue

            map[ ii, jj] = int( c )

    return map


def checkMove( p0, p1, map):

    nRows, nCols = map.shape

    ii = p0[0]
    jj = p0[1]

    nextII = p1[0]
    nextJJ = p1[1]

    if nextII < 0 or nextII >= nRows: return False
    if nextJJ < 0 or nextJJ >= nCols: return False

    currentHeight = map[ ii, jj]
    nextHeight = map[ nextII, nextJJ]
    change = nextHeight - currentHeight

    if change != 1: return False

    return True


def travel( p0, map):

    paths = [ [p0] ]

    while True:

        nextPaths = []

        for path in paths:
            for move in moves:

                p0 = path[-1]
                nextPosition = p0 + move
                validMove = checkMove( p0, nextPosition, map)

                if not validMove: continue
                
                nextPath = path.copy()
                nextPath.append( nextPosition )
                nextPaths.append( nextPath.copy() )

        if len( nextPaths ) == 0: break
        paths = nextPaths     
        
    uniqueStops = [ tuple( path[-1] ) for path in paths]
    uniqueStops = set( uniqueStops )

    score = len( uniqueStops )
    rating = len( paths )

    return paths, score, rating


def getHikingTrails( map ):

    allPaths = []
    ratings = []
    scores = []

    startLocations = np.argwhere( map == 0 )

    for p in startLocations:

        paths, score, rating = travel( p, map)

        allPaths.append( paths )
        ratings.append( rating )
        scores.append( score )

    return allPaths, scores, ratings



