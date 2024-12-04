import xmas

file = open("./day4/data.txt")
lines = file.readlines()

data = xmas.parse( lines )
totalXMAS = xmas.countXMAS( data )
totalMASMAS = xmas.countMASMAS( data )

print( totalXMAS )
print( totalMASMAS )