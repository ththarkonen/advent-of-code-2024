import mapTools

file = open("./day10/data.txt")
lines = file.readlines()

map = mapTools.parse( lines )
paths, scores, ratings = mapTools.getHikingTrails( map )

totalScore = sum( scores )
totalRating = sum( ratings )

print( totalScore )
print( totalRating )