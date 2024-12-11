import stoneLib

file = open("./day11/data.txt")
lines = file.readline()

stones = stoneLib.parse( lines )
totalBlinks = 75

for _ in range( totalBlinks ):
    stones = stoneLib.blink( stones )

print( stones.total() )
