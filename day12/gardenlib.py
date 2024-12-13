import numpy as np
import kernelslib
from scipy.signal import convolve2d

moves = ( np.array([-1, 0]), np.array([ 0, 1]),
          np.array([ 1, 0]), np.array([ 0,-1]) )

kernels = kernelslib.get()

def parse( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    dims = ( nRows, nCols)
    data = np.zeros( dims )

    for ii, line in enumerate( lines ):
        for jj, c in enumerate( line ):
            if c == "\n": continue

            data[ ii, jj] = ord( c )

    return data

def checkPlantValidity( plant, plot, plantPlots):

    if plant in plot: return False

    for plots in plantPlots:
        for plot in plots:
            if plant == plot: return False

    return True


def checkMove( p0, p1, plot, plots, map):

    p0 = tuple( p0 )
    p1 = tuple( p1 )

    nRows, nCols = map.shape

    ii = p0[0]
    jj = p0[1]

    nextII = p1[0]
    nextJJ = p1[1]

    if nextII < 0 or nextII >= nRows: return False
    if nextJJ < 0 or nextJJ >= nCols: return False

    currentPlant = map[ ii, jj]
    nextPlant = map[ nextII, nextJJ]

    if nextPlant != currentPlant: return False

    nextPosition = ( nextII, nextJJ)
    validPlant = checkPlantValidity( nextPosition, plot, plots)

    if not validPlant: return False

    return True


def fillPlot( p, plantPlots, map):

    ii = int( p[0] )
    jj = int( p[1] )

    nextPlot = [ ( ii, jj) ]

    while True:
        
        plot = nextPlot.copy()
        noNewLocations = True

        for plantPosition in plot:
            for move in moves:

                p0 = plantPosition
                p1 = p0 + move
                validMove = checkMove( p0, p1, nextPlot, plantPlots, map)

                if not validMove: continue

                nextII = int( p1[0] )
                nextJJ = int( p1[1] )

                nextPlot.append( (nextII, nextJJ) )
                noNewLocations = False

        if noNewLocations: break

    return nextPlot

def getPlotsForPlant( plant, map):

    plantPlots = []
    plantLocations = np.argwhere( map == plant )

    for p in plantLocations:

        validPlant = checkPlantValidity( tuple( p ), [], plantPlots)
        if not validPlant: continue

        plot = fillPlot( p, plantPlots, map)
        plantPlots.append( plot.copy() )

    return plantPlots


def getPlots( map ):

    plots = {}
    uniquePlants = np.unique( map )

    for plant in uniquePlants:

        plantPlots = getPlotsForPlant( plant, map)
        plots[ plant ] = plantPlots

    return plots


def computeFencing( plot ):

    fencingLength = 0

    for p in plot:

        ii = p[0]
        jj = p[1]

        for move in moves:

            nextII = ii + move[0]
            nextJJ = jj + move[1]
            nextPosition = ( nextII, nextJJ)

            if nextPosition not in plot:
                fencingLength += 1

    return fencingLength


def computeSides( plot, map):

    nRows, nCols = map.shape
    dims = ( nRows, nCols)
    plantMap = np.zeros( dims )

    for ii, jj in plot:
        plantMap[ ii, jj] = 1

    plantMap = np.trim_zeros( plantMap )
    totalCorners = 0

    for kernel, value, multiplier in kernels:
        
        corners = convolve2d( plantMap, kernel, "same")
        corners = corners == value

        totalCorners += multiplier * np.sum( corners )

    return totalCorners


def computePrice( plantPlots, map):

    fencings = []
    areas = []
    sides = []

    price = 0
    priceBulk = 0

    for plant in plantPlots:
        for plot in plantPlots[ plant ]:

            fencingLength = computeFencing( plot )
            sideNumber = computeSides( plot, map)
            area = len( plot )
            
            fencings.append( fencingLength )
            areas.append( area )
            sides.append( sideNumber )

            price += area * fencingLength
            priceBulk += area * sideNumber

    return price, priceBulk
            




