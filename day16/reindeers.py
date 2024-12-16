import olympics

file = open("./day16/data.txt")
lines = file.readlines()

maze, start, stop = olympics.parse( lines )
scores, paths = olympics.travel( maze, start, stop)

topScore = olympics.getTopScore( scores, stop)
seats = olympics.getSeats( paths, stop, topScore)

print( topScore )
print( len( seats ) )