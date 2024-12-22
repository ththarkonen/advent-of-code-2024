import functools

def parse( fileContents ):

    patterns, designs = fileContents.split("\n\n")
    patterns = patterns.replace("\n", "")
    patterns = patterns.replace(" ", "")
    patterns = patterns.split(",")
    patterns = set( patterns )

    designs = designs.split("\n")

    return patterns, designs

@functools.cache
def checkDesign( design, patterns):

    isValid = 0

    for pattern in patterns:

        nPattern = len( pattern )
        nDesign = len( design )

        if nPattern > nDesign: continue

        subdesign = design[0:nPattern]

        patternExists = subdesign == pattern
        endOfDesign = nDesign == nPattern

        if patternExists and endOfDesign:
            isValid += 1
        if patternExists and not endOfDesign:
            tempIsValid = checkDesign( design[nPattern:], patterns)
            isValid += tempIsValid
    
    return isValid


def removeRedundantPatters( patterns ):

    neededPatterns = set()
    redundantPatterns = set()

    for pattern in patterns:

        tempPatterns = patterns.copy()
        tempPatterns.remove( pattern )
        tempPatterns = frozenset( tempPatterns )

        composable = checkDesign( pattern, tempPatterns)
        if not composable:
            neededPatterns.add( pattern )
        else:
            redundantPatterns.add( pattern )

    return neededPatterns, redundantPatterns


def checkDesigns( designs, patterns):

    possibleDesigns = []
    decompositions = []

    for design in designs:

        validRedundants = findValidRedundants( design, patterns)
        composable = checkDesign( design, validRedundants)

        if composable:
            possibleDesigns.append( design )
            decompositions.append( composable )

    return possibleDesigns, decompositions


def findValidRedundants( pattern, redundantPatterns):

    valids = []

    for r in redundantPatterns:
        if r in pattern:
            valids.append( r )

    return frozenset( valids )