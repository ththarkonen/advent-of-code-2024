import gps

file = open("./day15/data.txt")
fileContents = file.read()

layout, moves = gps.parse( fileContents )
layoutWide = gps.parseWide( fileContents )

layout = gps.simulateRobot( layout, moves)
layoutWide = gps.simulateRobotWide( layoutWide, moves)

coordinates = gps.coordinates( layout )
coordinatesWide = gps.coordinates( layoutWide )

print( sum( coordinates ) )
print( sum( coordinatesWide ) )