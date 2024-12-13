def parse( lines, checkCondition):

    muls = []

    for line in lines:

        line = line.split("mul")
        muls.extend( line )

    operations = []
    doPrevious = True

    for mulArgument in muls:

        do = doPrevious

        if checkCondition:
            doPrevious = updateCondition( mulArgument, doPrevious)
                
        mulArgument = mulArgument.split(",")

        if len( mulArgument ) < 2: continue

        firstArgument = mulArgument[0]
        secondArgument = mulArgument[1]

        if ")" not in secondArgument: continue

        notCorrupted = firstArgument[0] == "("

        firstArgument = firstArgument[1:]
        secondArgument = secondArgument.split(")")[0]

        notCorrupted = notCorrupted and firstArgument.isdigit()
        notCorrupted = notCorrupted and secondArgument.isdigit()
            
        if notCorrupted and do:

            leftNumber = int( firstArgument )
            rightNumber = int( secondArgument )

            operation = {}
            operation["type"] = "mul"
            operation["args"] = ( leftNumber, rightNumber)

            operations.append( operation )
        
    return operations


def updateCondition( mulArgument, doPrevious):

    reversedDo = ")(od"
    reversedDont = ")(t'nod"

    if "do()" in mulArgument:
        doIndex = mulArgument[::-1].index( reversedDo )
    else:
        doIndex = None

    if "don't()" in mulArgument:
        dontIndex = mulArgument[::-1].index( reversedDont )
    else:
        dontIndex = None

    if dontIndex is not None: doPrevious = False
    if doIndex is not None: doPrevious = True
    if doIndex is not None and dontIndex is not None and doIndex < dontIndex: doPrevious = True
    if doIndex is not None and dontIndex is not None and doIndex > dontIndex: doPrevious = False

    return doPrevious


def computeOperations( operations ):

    total = 0

    for op in operations:
        if op["type"] == "mul":

            x = op["args"][0]
            y = op["args"][1]

            total += x * y

    return total

