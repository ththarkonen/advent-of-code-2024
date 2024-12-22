import linenlib

file = open("./day19/data.txt")
fileContents = file.read()

patterns, designs = linenlib.parse( fileContents )
minimumPatterns, otherPatterns = linenlib.removeRedundantPatters( patterns )
possibleDesigns, decompositions = linenlib.checkDesigns( designs, patterns)

totalDesigns = len( possibleDesigns )
totalIterations = sum( decompositions )

print( totalDesigns )
print( totalIterations )