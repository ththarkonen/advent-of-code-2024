import padlib

file = open("./day21/data.txt")
lines = file.readlines()
codes = padlib.parse( lines )

minimumLengths2 = padlib.checkCodes( codes, 2)
minimumLengths25 = padlib.checkCodesPart2( codes, 25)

result = padlib.computeResult( codes, minimumLengths2)
result2 = padlib.computeResult( codes, minimumLengths25)

print( result )
print( result2 )