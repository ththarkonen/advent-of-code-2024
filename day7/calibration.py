from itertools import product

operations = ["+", "*"]
operationsWithConcat = ["+", "*", "||"]

def parse( lines ):

    calibrationNumbers = []
    operationNumbers = []

    for line in lines:
        
        line = line.replace("\n", "")
        line = line.split(":")

        numbers = line[1].split(" ")[1:]

        calibrationNumber = int( line[0] )
        numbers = [ int(d) for d in numbers ]

        calibrationNumbers.append(calibrationNumber )
        operationNumbers.append( numbers )

    return calibrationNumbers, operationNumbers


def operate( numbers, operations):

    result = None

    for ii, op in enumerate( operations ):

        if op == "+":
            if ii == 0:
                result = numbers[0] + numbers[1]
            else:
                result = result + numbers[ii + 1]

        elif op == "*":
            if ii == 0:
                result = numbers[0] * numbers[1]
            else:
                result = result * numbers[ii + 1]

        elif op == "||":
            if ii == 0:
                result = str( numbers[0] ) + str( numbers[1] )
                result = int( result )
            else:
                result = str( result ) + str( numbers[ii + 1] )
                result = int( result )

    return result


def getValids( calibrationNumbers, operationNumbers, withConcat = False):

    validCalibrationNumbers = []

    for ii, c in enumerate( calibrationNumbers ):

        nums = operationNumbers[ii]
        nNums = len( nums )

        if withConcat:
            allOperations = product( operationsWithConcat, repeat = nNums - 1)
        else:
            allOperations = product( operations, repeat = nNums - 1)

        for ops in allOperations:
            if c == operate( nums, ops):
                validCalibrationNumbers.append( c )
                break

    return validCalibrationNumbers





