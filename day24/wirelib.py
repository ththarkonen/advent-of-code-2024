
def parse( fileContents ):

    fileContents = fileContents.split("\n\n")
    initialConditions = fileContents[0]
    gates = fileContents[1]

    system = {}
    system["wires"] = {}
    system["gates"] = {}

    for line in initialConditions.split("\n"):

        line = line.split(": ")

        wire = line[0]
        bit = int( line[1] )

        system["wires"][ wire ] = bool( bit )

    for line in gates.split("\n"):

        line = line.replace("\n","")
        line = line.replace("-> ", "")
        line = line.split(" ")

        inputLeft = line[0]
        inputRight = line[2]
        operation = line[1]
        outputWire = line[3]

        if operation == "AND": opLambda = lambda x, y: x & y == True
        if operation ==  "OR": opLambda = lambda x, y: x | y
        if operation == "XOR": opLambda = lambda x, y: x ^ y

        system["wires"][ outputWire ] = None

        system["gates"][ outputWire ] = {}
        system["gates"][ outputWire ]["inputs"] = [ inputLeft, inputRight]
        system["gates"][ outputWire ]["operation"] = opLambda
        system["gates"][ outputWire ]["opSymbol"] = operation

    return system


def operate( wires, gate):

    x = gate["inputs"][0]
    y = gate["inputs"][1]

    x = wires[x]
    y = wires[y]

    if x == None or y == None:
        return None

    return gate["operation"](x,y)


def run( system ):

    operations = 1

    while operations:

        operations = 0

        for wire in system["wires"]:
            if system["wires"][ wire ] is not None: continue

            output = operate( system["wires"], system["gates"][ wire ])
            system["wires"][ wire ] = output

            operations += 1

    return system


def format( system, marker = "z"):

    wires = [ wire for wire in system["wires"] if wire[0] == marker ]
    wires = sorted( wires, reverse = True)

    bits = [ system["wires"][ wire ] for wire in wires ]

    if None in bits:
        return None, wires

    bits = [ int( bit ) for bit in bits ]
    bits = [ str( bit ) for bit in bits ]
    bits = "".join( bits )

    outputDecimal = int( bits, 2)
    return outputDecimal


def getBadWires( system ):

    weirdGates = []

    for gate in system["gates"]:

        if gate[0] == "z" and system["gates"][gate]["opSymbol"] != "XOR" and gate != "z45":
            weirdGates.append( gate )

        if system["gates"][gate]["opSymbol"] != "AND":
            inputs = system["gates"][gate]["inputs"]
            inputLeft = inputs[0]
            inputRight = inputs[1]

            if inputLeft[0] == "x" and inputRight[0] != "y":
                weirdGates.append( gate )

            if inputLeft[0] != "x" and inputRight[0] == "y":
                weirdGates.append( gate )

        if system["gates"][gate]["opSymbol"] == "OR":
            inputs = system["gates"][gate]["inputs"]
            inputLeft = inputs[0]
            inputRight = inputs[1]

            opLeft = system["gates"][inputLeft]["opSymbol"]
            opRight = system["gates"][inputRight]["opSymbol"]

            if opLeft != "AND":
                weirdGates.append( inputLeft )

            if opRight != "AND":
                weirdGates.append( inputRight )

        if system["gates"][gate]["opSymbol"] == "XOR" and gate[0] != "z":

            inputs = system["gates"][gate]["inputs"]
            inputLeft = inputs[0]
            inputRight = inputs[1]

            if inputLeft[0] == "x" or inputLeft[0] == "y" and inputRight[0] == "x" or inputRight[0] == "y":
                pass
            else:
                weirdGates.append( gate )
                

        if system["gates"][gate]["opSymbol"] == "XOR" and gate != "z01":
            inputs = system["gates"][gate]["inputs"]
            inputLeft = inputs[0]
            inputRight = inputs[1]

            if inputLeft[0] != "x" and inputLeft[0] != "y":

                opLeft = system["gates"][inputLeft]["opSymbol"]

                if opLeft == "AND":
                    weirdGates.append( inputLeft )

            if inputRight[0] != "x" and inputRight[0] != "y":

                opRight = system["gates"][inputRight]["opSymbol"]

                if opRight == "AND":
                    weirdGates.append( inputRight )

    weirdGates = set( weirdGates )
    weirdGates = sorted( weirdGates )

    return weirdGates