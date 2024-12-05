import numpy as np

def parse( lines ):

    firstSection = True

    pageConditions = []
    pages = []

    for line in lines:

        line = line.replace("\n", "")
        
        if line == "":
            firstSection = False
            continue

        if firstSection:

            line = line.split("|")
            row = [ int(d) for d in line]
            pageConditions.append( row )
        else:

            line = line.split(",")
            row = [ int(d) for d in line]
            row = np.array( row )
            pages.append( row )

    pageConditions = np.array( pageConditions )
    return pageConditions, pages


def constructOrdering( pageConditions ):

    pageOrdering = {}

    for condition in pageConditions:

        left = condition[0]
        right = condition[1]

        if left in pageOrdering:
            pageOrdering[left].append( right )
        else:
            pageOrdering[left] = [ right ]

    return pageOrdering


def getCorrectPages( pageSets, pageOrdering):

    correctPageSets = []
    incorrectPageSets = []

    for pageSet in pageSets:
        for ii, page in enumerate( pageSet[1:] ):

            if page not in pageOrdering: continue
            prevPages = pageSet[ :ii+1 ]

            correctOrdering = ~np.in1d( prevPages, pageOrdering[page])
            correctOrdering = np.all( correctOrdering )

            if not correctOrdering: break

        if correctOrdering:
            correctPageSets.append( pageSet )
        else:
            incorrectPageSets.append( pageSet )

    return correctPageSets, incorrectPageSets


def shiftPages( pageSet, ii, inds):

    currentPage = pageSet[ ii+1 ]
    correctLeftPages = pageSet[ :ii+1 ][ inds ]
    incorrectLeftPages = pageSet[ :ii+1 ][ ~inds ]
    rightPages = pageSet[ ii+2: ]

    shiftedPages = np.append( correctLeftPages, currentPage)
    shiftedPages = np.append( shiftedPages, incorrectLeftPages)
    shiftedPages = np.append( shiftedPages, rightPages)

    return shiftedPages


def sortIncorrectSets( pageSets, pageOrdering):

    sortedPageSets = []

    for pageSet in pageSets:

        correctOrdering = False

        while not correctOrdering:
            for ii, page in enumerate( pageSet[1:] ):

                if page not in pageOrdering: continue
                prevPages = pageSet[ :ii+1 ]

                correctOrderingInds = ~np.in1d( prevPages, pageOrdering[page])
                correctOrdering = np.all( correctOrderingInds )

                if not correctOrdering:
                    pageSet = shiftPages( pageSet, ii, correctOrderingInds)
                    break

        sortedPageSets.append( pageSet )

    return sortedPageSets


def countMiddlePages( pageSets ):

    total = 0

    for pageSet in pageSets:

        n = len( pageSet )
        middleIndex = int( 0.5 * n - 0.5 )

        total += pageSet[ middleIndex ]

    return total