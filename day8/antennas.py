import numpy as np
from itertools import combinations

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    data = np.zeros( dims )

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):

            if c == ".": continue
            if c == "\n": continue

            data[ ii, jj] = ord( c )

    return data


def computeAntinodes( data ):

    nRows, nCols = data.shape

    uniqueValues = np.unique( data )
    uniqueValues = uniqueValues[ uniqueValues != 0 ]

    antinodes = []

    for d in uniqueValues:

        inds = np.argwhere( data == d )

        for pair in combinations( inds, 2):
            
            x = pair[0]
            y = pair[1]

            v = x - y
            antinodeX = x + v
            antinodeY = y - v
            possibleAntinodes = ( antinodeX, antinodeY)

            for antinode in possibleAntinodes:

                ii = antinode[0]
                jj = antinode[1]
                node = ( ii, jj)

                if ii < 0 or ii >= nRows: continue
                if jj < 0 or jj >= nCols: continue
                if node in antinodes: continue

                antinodes.append( node )

    return antinodes


def computeHarmonics( pair, antinodes, dims):

    nRows = dims[0]
    nCols = dims[1]
            
    x = pair[0]
    y = pair[1]

    v = x - y
    direction = -1

    for point in pair:

        direction = -1 * direction
        step = 0
        
        while True:

            antinode = point + direction * step * v

            ii = antinode[0]
            jj = antinode[1]
            node = ( ii, jj)
            
            step = step + 1

            if ii < 0 or ii >= nRows: break
            if jj < 0 or jj >= nCols: break
            if node in antinodes: continue

            antinodes.append( node )

    return antinodes


def computeHarmonicAntinodes( data ):

    uniqueValues = np.unique( data )
    uniqueValues = uniqueValues[ uniqueValues != 0 ]

    antinodes = []

    for d in uniqueValues:

        inds = np.argwhere( data == d )

        for pair in combinations( inds, 2):
            antinodes = computeHarmonics( pair, antinodes, data.shape)

    return antinodes