import numpy as np

def parse( fileContents ):

    keysLocks = fileContents.split("\n\n")

    nRows = len( keysLocks[0].split("\n") )
    nCols = len( keysLocks[0].split("\n")[0] )

    dims = ( nRows, nCols)

    keys = []
    locks = []

    for keylock in keysLocks:
        
        schematic = np.zeros( dims )
        keylock = keylock.split("\n")

        isKey = True
        if keylock[0][0] == "#": isKey = False

        for ii, line in enumerate( keylock ):
            for jj, c in enumerate( line ):
                if c == "#":
                    schematic[ii][jj] = 1

        if isKey:
            keys.append( schematic )
        else:
            locks.append( schematic )

    return keys, locks


def checkKey( key, lock):

    nRows, nCols = key.shape

    for jj in range( nCols ):

        keyCol = key[:,jj]
        lockCol = lock[:,jj]

        keyHeight = sum( keyCol ) - 1
        lockHeight = sum( lockCol ) - 1

        if keyHeight + lockHeight > nRows - 2:
            return False
    
    return True


def checkKeys( keys, locks):

    validCombinations = []

    for key in keys:
        for lock in locks:

            validPair = checkKey( key, lock)
            validCombinations.append( validPair )

    return validCombinations
    