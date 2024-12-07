import calibration

file = open("./day7/data.txt")
lines = file.readlines()

calibrationNumbers, opNumbers = calibration.parse( lines )
valids = calibration.getValids( calibrationNumbers, opNumbers)
validsWithConcat = calibration.getValids( calibrationNumbers, opNumbers, withConcat = True)

result = sum( valids )
resultConcat = sum( validsWithConcat )

print( result )
print( resultConcat )