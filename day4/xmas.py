import numpy as np
import itertools

encoding = {"X": "0 ",
            "M": "1 ",
            "A": "2 ",
            "S": "3 "}

directions = itertools.permutations( [-1, -1, 0, 1, 1], 2)
directions = set( directions )
directions = list( directions )
directions = np.array( directions )

directionsMASMAS = directions[ [ 1, 2, 3, 4], :]
directionsMASMAS = np.append( directionsMASMAS, [[ 0, 0]], axis = 0)

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines )

    dims = ( nRows, nCols)
    data = np.empty( dims )

    for ii, line in enumerate( lines ):

        line = line.replace("\n", "")
        
        for e in encoding:
            line = line.replace( e, encoding[e])
        
        line = line.split(" ")[:-1]
        data[ ii, :] = np.array( line )

    return data


def makeCheckInds( direction ):
    # Should precompute these

    dims = ( 4, 2)
    inds = np.zeros( dims, dtype = int)

    for ii in range( 1, 4):
        inds[ ii, :] = ii * direction

    return inds


def countXMAS( data ):

    nRows, nCols = data.shape
    startInds = np.argwhere( data == 0 )
    total = 0

    for p0 in startInds:
        for d in directions:

            checkInds = makeCheckInds( d ) + p0
            ii = checkInds[ :, 0]
            jj = checkInds[ :, 1]

            if np.any( ii < 0) or np.any( ii >= nRows): continue
            if np.any( jj < 0) or np.any( jj >= nCols): continue

            if np.all( data[ ii, jj] == [ 0, 1, 2, 3] ):
                total += 1

    return total


def countMASMAS( data ):

    nRows, nCols = data.shape
    startInds = np.argwhere( data == 2 )
    total = 0

    for p0 in startInds:

        checkInds = directionsMASMAS + p0
        ii = checkInds[ :, 0]
        jj = checkInds[ :, 1]

        if np.any( ii < 0 ) or np.any( ii >= nRows ): continue
        if np.any( jj < 0 ) or np.any( jj >= nCols ): continue

        leftTopInds = checkInds[ [ 1, 4, 3], :]
        leftBotInds = checkInds[ [ 0, 4, 2], :]

        leftTopII = leftTopInds[ :, 0]
        leftTopJJ = leftTopInds[ :, 1]

        leftBotII = leftBotInds[ :, 0]
        leftBotJJ = leftBotInds[ :, 1]

        leftTop = data[ leftTopII, leftTopJJ]
        leftBot = data[ leftBotII, leftBotJJ]

        leftTopMAS = np.all( leftTop == [ 1, 2, 3] ) or np.all( leftTop == [ 3, 2, 1] )
        leftBotMAS = np.all( leftBot == [ 1, 2, 3] ) or np.all( leftBot == [ 3, 2, 1] )

        if leftTopMAS and leftBotMAS:
            total += 1

    return total