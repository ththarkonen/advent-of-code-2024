
import numpy as np

def parse( data ):

    mapStr, movesStr = data.split("\n\n")
    mapStr = mapStr.split("\n")

    nRows = len( mapStr )
    nCols = len( mapStr[0] )

    dims = ( nRows, nCols)
    layout = np.zeros( dims )

    for ii, line in enumerate( mapStr ):
        for jj, c in enumerate( line ):
            
            if c == "#": layout[ ii, jj] = -1
            if c == "O": layout[ ii, jj] =  1
            if c == "@": layout[ ii, jj] =  2

    moves = movesStr.replace("\n", "")

    return layout, moves


def parseWide( data ):

    mapStr, _ = data.split("\n\n")
    mapStr = mapStr.split("\n")

    nRows = len( mapStr )
    nCols = len( mapStr[0] )

    dims = ( nRows, 2 * nCols)
    layout = np.zeros( dims )

    for ii, line in enumerate( mapStr ):
        for jj, c in enumerate( line ):
            
            if c == "#":
                layout[ ii, 2 * jj] = -1
                layout[ ii, 2 * jj + 1] = -1

            if c == "O":
                layout[ ii, 2 * jj] =  1
                layout[ ii, 2 * jj + 1] =  3
            
            if c == "@":
                layout[ ii, 2 * jj] =  2

    return layout

def moveBoxes( layout, move):

    if move == ">": nRotations = 0
    elif move == "v": nRotations = 1
    elif move == "<": nRotations = 2
    elif move == "^": nRotations = 3

    layout = np.rot90( layout, nRotations)
    robot = np.argwhere( layout == 2 )
    
    ii = robot[0][0]
    jj = robot[0][1]
    row = layout[ ii, :]

    nextNonBox = layout[ ii, :] != 1
    nonBoxInds = np.argwhere( nextNonBox )
    validInds = nonBoxInds > jj
    validInd = nonBoxInds[ validInds ][0]

    notWall = row[ validInd ] != -1

    if notWall:

        interval = row[ jj:validInd ]
        nBoxes = sum( interval == 1 )

        newRobotJJ = jj + 1

        boxStart = jj + 2
        boxStop = jj + 2 + nBoxes

        layout[ ii, jj:validInd] = 0
        layout[ ii, boxStart:boxStop] = 1
        layout[ ii, newRobotJJ] = 2

    layout = np.rot90( layout, 4 - nRotations)

    return layout


def getBoxShape( ii, jj, boxSide, nRotations):

    if nRotations % 2 == 0:
        return [( ii, jj + 1, boxSide)]
    
    if nRotations == 1 and boxSide == 1:

        pNextLeft = ( ii, jj + 1, 1)
        pNextRight = ( ii - 1, jj + 1, 3)

        return [ pNextLeft, pNextRight]
    
    if nRotations == 3 and boxSide == 1:

        pNextLeft = ( ii, jj + 1, 1)
        pNextRight = ( ii + 1, jj + 1, 3)
    
    if nRotations == 1 and boxSide == 3:

        pNextLeft = ( ii + 1, jj + 1, 1)
        pNextRight = ( ii, jj + 1, 3)

        return [ pNextLeft, pNextRight]
    
    if nRotations == 3 and boxSide == 3:

        pNextLeft = ( ii - 1, jj + 1, 1)
        pNextRight = ( ii, jj + 1, 3)

    return [ pNextLeft, pNextRight]


def getShapeLayer( locations, layout, nRotations):

    newLocations = []

    blocked = False
    
    for p in locations:

        ii = p[0]
        jj = p[1]

        nextSpotType = layout[ ii, jj + 1]

        if nextSpotType == -1:
            blocked = True
            return [], blocked
        
        if nextSpotType == 1 or nextSpotType == 3:
            newLocations += getBoxShape( ii, jj, nextSpotType, nRotations)
            

    return newLocations, blocked


def moveWideBoxes( layout, move):

    if move == ">": nRotations = 0
    elif move == "v": nRotations = 1
    elif move == "<": nRotations = 2
    elif move == "^": nRotations = 3

    layout = np.rot90( layout, nRotations)
    robot = np.argwhere( layout == 2 )
    
    ii = robot[0][0]
    jj = robot[0][1]

    p = [( ii, jj, 2)]

    shape = []
    shape = shape + p.copy()

    while True:

        pNext, blocked = getShapeLayer( p, layout, nRotations)
        
        if blocked: break
        if len( pNext ) == 0: break

        p = pNext
        shape += pNext.copy()

    if not blocked:

        for p in shape:

            ii = p[0]
            jj = p[1]

            layout[ ii, jj] = 0

        for p in shape:

            ii = p[0]
            jj = p[1]
            objectType = p[2]

            layout[ ii, jj + 1] = objectType

        p = pNext

    layout = np.rot90( layout, 4 - nRotations)

    return layout


def simulateRobot( layout, moves):

    for move in moves:
        layout = moveBoxes( layout, move)

    return layout


def simulateRobotWide( layout, moves):

    history = [ layout ]

    for move in moves:
        layout = moveWideBoxes( layout, move)
        history.append( layout.copy() )

    return layout, history


def coordinates( layout ):

    coordinates = []
    boxes = np.argwhere( layout == 1 )

    for box in boxes:
        
        coordinate = 100 * box[0] + box[1]
        coordinates.append( coordinate )

    return coordinates