import numpy as np

def parse( lines ):

    lines = lines
    nLines = len( lines )

    columnDims = ( nLines, 1)
    leftColumn = np.empty( columnDims )
    rightColumn = np.empty( columnDims )

    for ii in range( nLines ):

        line_ii = lines[ii]

        line_ii = line_ii.replace("\n","")
        line_ii = line_ii.split("   ")

        leftColumn[ii] = int( line_ii[0] )
        rightColumn[ii] = int( line_ii[1] )

    return leftColumn, rightColumn


def match( data ):

    leftColumn = data[0]
    rightColumn = data[1]

    leftColumn = np.sort( leftColumn, axis = 0)
    rightColumn = np.sort( rightColumn, axis = 0)

    return leftColumn, rightColumn


def computeDistance( data ):

    leftColumn = data[0]
    rightColumn = data[1]

    distances = np.abs( leftColumn - rightColumn )
    totalDistance = np.sum( distances )
    totalDistance = int( totalDistance )

    return totalDistance


def computeSimilarityScore( data ):

    leftColumn = data[0]
    rightColumn = data[1]

    similarityScore = 0

    for leftValue in leftColumn:

        leftValue = leftValue[0]

        occurancesInRight = np.sum( rightColumn == leftValue )
        similarityScore += occurancesInRight * leftValue

    similarityScore = int( similarityScore )
    return similarityScore


