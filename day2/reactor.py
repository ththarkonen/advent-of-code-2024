import levels

file = open("./day2/data.txt")
lines = file.readlines()

data = levels.parse( lines )

safeLevels = levels.analyzeSafety( data )
safeLevels = levels.analyzeDampenedSafety( data )

totalSafeLevels = sum( safeLevels )

print( totalSafeLevels )
