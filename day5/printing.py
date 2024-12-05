import pages

file = open("./day5/data.txt")
lines = file.readlines()

pageConditions, pageSets = pages.parse( lines )
pageOrdering = pages.constructOrdering( pageConditions )
correctPageSets, incorrectPageSets = pages.getCorrectPages( pageSets, pageOrdering)

incorrectPageSets = pages.sortIncorrectSets( incorrectPageSets, pageOrdering)

total = pages.countMiddlePages( correctPageSets )
totalSorted = pages.countMiddlePages( incorrectPageSets )


print( total )
print( totalSorted )