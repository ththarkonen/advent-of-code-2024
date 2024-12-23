import networklib as networklib

file = open("./day23/data.txt")
lines = file.readlines()

connections = networklib.parse( lines )
loops = networklib.getLoops( connections )
validLoops = networklib.filterLoops( loops )
networks = networklib.findNetworks( loops, connections)
largestNetwork = networklib.getLargestNetwork( networks )

totalLoopsT = len( validLoops )

print( totalLoopsT )
print( largestNetwork )
