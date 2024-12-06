import guardMap

file = open("./day6/data.txt")
lines = file.readlines()

guard, map = guardMap.parse( lines )

guardPositions = guardMap.simulate( guard.copy(), map)
blockPositions = guardMap.getLoopingBlocks( guardPositions, guard.copy(), map)

uniquePositions = len( guardPositions )
loopBlockLocations = len( blockPositions )

print( uniquePositions )
print( loopBlockLocations )