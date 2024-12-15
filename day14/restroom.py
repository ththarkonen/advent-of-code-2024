import robotlib

file = open("./day14/data.txt")
lines = file.readlines()

T = 10000
limits = [ 101, 103]

robotsInit = robotlib.parse( lines )
robots = robotlib.simulate( robotsInit, 100, limits)
robotsInQuadrants, result = robotlib.quadrants( robots, limits)

losses = robotlib.findChristmasTree( robotsInit, T, limits)
maxLoss = max( losses )
secondsUntillTree = losses.index( maxLoss ) + 1

print( result )
print( secondsUntillTree )