import bytelib

file = open("./day18/data.txt")
lines = file.readlines()

memoryLimits = (71, 71)
bytes = bytelib.parse( lines )
path = bytelib.dodge( bytes, memoryLimits, 1024)
lastByte = bytelib.getLastPath( bytes, memoryLimits, 1024)

steps = path[-1]

print( steps )
print( lastByte )
