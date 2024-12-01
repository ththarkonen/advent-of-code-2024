import history

file = open("./day1/data.txt")
lines = file.readlines()

data = history.parse( lines )
dataSorted = history.match( data )

distance = history.computeDistance( dataSorted )
similarityScore = history.computeSimilarityScore( dataSorted )

print( distance )
print( similarityScore )





