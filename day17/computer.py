import numpy as np

def parse( lines ):

    registerStr, program = lines.split("\n\n")
    registerStr = registerStr.replace("\n", " ")
    registerStr = registerStr.split(" ")

    program = program.replace(" ", ",")
    program = program.split(",")
    program = program[1:]

    register = {}
    register["A"] = int( registerStr[2] )
    register["B"] = int( registerStr[5] )
    register["C"] = int( registerStr[8] )

    program = [ int(d) for d in program ]

    return register, program


def operate( opcode, literal, register):

    combo = literal

    if literal == 4:
        combo = register["A"]
    if literal == 5:
        combo = register["B"]
    if literal == 6:
        combo = register["C"]

    if opcode == 0:
        register["A"] = register["A"] // 2 ** combo
    if opcode == 1:
        register["B"] = register["B"] ^ literal
    if opcode == 2:
        register["B"] = combo % 8
    if opcode == 3:
        if register["A"] != 0: return literal
    if opcode == 4:
        register["B"] = register["B"] ^ register["C"]
    if opcode == 5:
        return str( combo % 8 )
    if opcode == 6:
        register["B"] = register["A"] // 2 ** combo
    if opcode == 7:
        register["C"] = register["A"] // 2 ** combo


def operate2( opcode, literal, register):

    combo = literal

    if literal == 4:
        combo = register["A"]
    if literal == 5:
        combo = register["B"]
    if literal == 6:
        combo = register["C"]

    if opcode == 0:
        register["A"] = register["A"] // 2 ** combo
    if opcode == 1:
        register["B"] = register["B"] ^ literal
    if opcode == 2:
        register["B"] = combo % 8
    if opcode == 3:
        if register["A"] != 0: return literal
    if opcode == 4:
        register["B"] = register["B"] ^ register["C"]
    if opcode == 5:
        return combo % 8
    if opcode == 6:
        register["B"] = register["A"] // 2 ** combo
    if opcode == 7:
        register["C"] = register["A"] // 2 ** combo
    

def run( program, register):

    instructionPointer = 0
    maxPointer = len( program )

    output = ""

    while instructionPointer < maxPointer - 1:

        opcode = program[ instructionPointer ]
        operand = program[ instructionPointer + 1 ]

        out = operate( opcode, operand, register)

        instructionPointer += 2

        if isinstance( out, str):
            output += "," + out

        if isinstance( out, int):
            instructionPointer = out

    return output[1:], register


def debug( program ):

    instructionPointer = 0
    maxPointer = len( program )

    register = {}
    register["A"] = 0
    register["B"] = 0
    register["C"] = 0

    shift = 2 ** ( 3 * (maxPointer-1) ) + 1
    step = 1
    counter = 0

    checkInd = 1

    while True:

        register["A"] = counter * step + shift
        register["B"] = 0
        register["C"] = 0

        output = []
        instructionPointer = 0

        while instructionPointer < maxPointer - 1:

            opcode = program[ instructionPointer ]
            operand = program[ instructionPointer + 1 ]

            out = operate2( opcode, operand, register)

            instructionPointer += 2

            if opcode == 5 and out is not None:
                output.append( out )

            if opcode == 3 and out is not None:
                instructionPointer = out

        if len( output ) <= len( program ):
            print( output )

        if np.all( output[0:checkInd] == program[0:checkInd] ):
            shift = counter * step + shift
            step = step * 4
            counter = 0
            checkInd += 1
        
        if np.all( output == program ):
            print( "output: ", output )
            print( "progra: ", program )
            print( shift - 1 )
            break

        counter += 1

    counter = 0
    while True:

        register["A"] = shift - counter
        register["B"] = 0
        register["C"] = 0

        output = []
        instructionPointer = 0

        while instructionPointer < maxPointer - 1:

            opcode = program[ instructionPointer ]
            operand = program[ instructionPointer + 1 ]

            out = operate2( opcode, operand, register)

            instructionPointer += 2

            if opcode == 5 and out is not None:
                output.append( out )

            if opcode == 3 and out is not None:
                instructionPointer = out

        if len( output ) < len( program ):
            print( output )
            break
        
        if np.all( output == program ):
            print( "output: ", output )
            print( "progra: ", program )
            print( shift - counter  )

        counter += 1
    
    return None