import corruption

file = open("./day3/data.txt")
lines = file.readlines()

operations = corruption.parse( lines, checkCondition = False)
operationsConditioned = corruption.parse( lines, checkCondition = True)

total = corruption.computeOperations( operations )
totalConditioned = corruption.computeOperations( operationsConditioned )

print( total )
print( totalConditioned )