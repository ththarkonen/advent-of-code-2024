import numpy as np
from scipy.signal import convolve2d

def parse( lines ):
    
    robots = []

    for line in lines:

        line = line.replace("p=", "")
        line = line.replace("v=", "")
        line = line.replace("\n", "")
        line = line.replace(",", " ")

        line = line.split(" ")
        
        x = int( line[0] )
        y = int( line[1] )

        vx = int( line[2] )
        vy = int( line[3] )

        robot = ( x, y, vx, vy)

        robots.append( robot )

    return robots


def simulate( robots, t, limits):

    result = []

    for robot in robots:

        x = robot[0]
        y = robot[1]

        vx = robot[2]
        vy = robot[3]

        x = ( x + vx * t ) % limits[0]
        y = ( y + vy * t ) % limits[1]

        result.append( ( x, y, vx, vy) )
    
    return result


def quadrants( robots, limits):

    middleX = limits[0] // 2
    middleY = limits[1] // 2

    totals = [ 0, 0, 0, 0]

    for robot in robots:

        x = robot[0]
        y = robot[1]

        if x < middleX and y < middleY:
            totals[0] += 1

        if x < middleX and y > middleY:
            totals[1] += 1

        if x > middleX and y > middleY:
            totals[2] += 1

        if x > middleX and y < middleY:
            totals[3] += 1

    result = 1
    for total in totals:
        result = total * result

    return totals, result


def findChristmasTree( robots, T, limits):

    nRows = limits[0]
    nCols = limits[1]
    dims = ( nRows, nCols)

    kernelDims = ( 5, 5)
    kernel = np.ones( kernelDims )

    losses = []

    for t in range( T ):

        data = np.zeros( dims )
        robots = simulate( robots, 1, limits)

        for robot in robots:

            ii = robot[0]
            jj = robot[1]

            data[ ii, jj] = 1
        
        loss = convolve2d( data, kernel, "same")
        loss = np.round( loss )
        loss = np.sum( loss )
        losses.append( loss )

        print( t )

    return losses
