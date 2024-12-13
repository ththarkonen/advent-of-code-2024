import clawlib

file = open("./day13/data.txt")
fileContent = file.read()

games = clawlib.parse( fileContent )
costs = clawlib.playOptimal( games )
costsError = clawlib.playOptimal( games, conversionError = True)

totalCost = sum( costs )
totalCostError = sum( costsError )

print( totalCost )
print( totalCostError )