import lib

file = open("./day25/data.txt")
lines = file.read()

keys, locks = lib.parse( lines )
matches = lib.checkKeys( keys, locks)
print( len(keys) )
print( len(locks) )
print( sum(matches) )