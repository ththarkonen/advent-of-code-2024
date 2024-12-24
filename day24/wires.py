import wirelib

file = open("./day24/data.txt")
fileContents = file.read()

system = wirelib.parse( fileContents )
system = wirelib.run( system )
output = wirelib.format( system, marker = "z")

badWires = wirelib.getBadWires( system )
result = ",".join( badWires )

print( output )
print( result )