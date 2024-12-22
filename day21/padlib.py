import functools
import moves
from collections import Counter

numpad = {}
keypad = {}

numpad[( 0, 0)] = "7"
numpad[( 0, 1)] = "8"
numpad[( 0, 2)] = "9"

numpad[( 1, 0)] = "4"
numpad[( 1, 1)] = "5"
numpad[( 1, 2)] = "6"

numpad[( 2, 0)] = "1"
numpad[( 2, 1)] = "2"
numpad[( 2, 2)] = "3"

numpad[( 3, 1)] = "0"
numpad[( 3, 2)] = "A"

keypad[( 0, 1)] = "^"
keypad[( 0, 2)] = "A"

keypad[( 1, 0)] = "<"
keypad[( 1, 1)] = "v"
keypad[( 1, 2)] = ">"

actions = ["^", ">", "v", "<", "A"]

mappings = moves.getMappings()

def parse( lines ):

    codes = []

    for line in lines:
    
        line = line.replace("\n","")
        codes.append( line )

    return codes

@functools.cache
def update( state, action):

    ii = state[0]
    jj = state[1]
    moves = state[2]
    code = state[-2]
    score = state[-1]

    stateUpdate = state[3:-1] + tuple([score])
    isNumpad = len( state ) == 5

    validState = True

    if action == "^":
        ii -= 1
        moves += 1
    if action == ">":
        jj += 1
        moves += 1
    if action == "v":
        ii += 1
        moves += 1
    if action == "<":
        jj -= 1
        moves += 1

    if action in "^>v<":
        if not isNumpad and ( ii, jj) not in keypad: return state, False
        if isNumpad and( ii, jj) not in numpad: return state, False

    if action == "A":

        padPress = state[0:2]
        moves = 0

        if isNumpad:
            if padPress not in numpad: return state, False
            code += numpad[ padPress ]
            stateUpdate = ( code, score)
        else:
            if padPress not in keypad: return state, False

            nextState = state[3:]
            nextAction = keypad[ padPress ]
            stateUpdate, validState = update( nextState, nextAction)

    nextState = ( ii, jj, moves) + stateUpdate
    return nextState, validState


def checkState( state, code, scores):

    input = state[-2]
    score = state[-1]
    key = state[0:-1]

    nInput = len( input )
    nState = len( state ) - 2
    indNumpad = nState - 3

    validState = True

    for ind in range( 0, nState - 2, 3):

        press = ( state[ ind ], state[ ind + 1 ])
        moveCount = state[ ind + 2 ]

        if ind == indNumpad:
            validState = press in numpad
        else:
            validState = press in keypad

        if not validState: return False

        if ind == indNumpad:
            validState = moveCount <= 4
        else:
            validState = moveCount <= 3

        if not validState: return False

    if input != code[0:nInput]: return False
    if nInput + 1 in scores and scores[ nInput + 1 ] <= score: return False
    if nInput not in scores: scores[ nInput ] = score
    if nInput in scores and scores[ nInput ] > score: scores[ nInput ] = score
    if key in scores and scores[ key ] <= score: return False

    scores[key] = score

    return True

def input( code, nKeypads = 2):

    start = ()

    for _ in range( nKeypads ):
        start += ( 0, 2, 0)

    start += ( 3, 2, 0, "", 0)

    nextStates = [ start ]
    scores =  {}

    counter = 1
    newStates = len( nextStates )
    while newStates:

        states = nextStates.copy()
        nextStates = []

        for state in states:
            for action in actions:

                nextState, validState = update( state, action)
                if not validState: continue

                nextState = nextState[0:-1] + tuple([ nextState[-1] + 1 ])
                validState = checkState( nextState, code, scores)

                if not validState: continue
                if validState:
                    nextStates.append( nextState )

                if nextState[-2] == code:
                    return nextState
                
        newStates = len( nextStates )
        if counter in scores:
            counter += 1
            nextStates = [ nextStates[-1] ]
        print( newStates )

    return []


def checkCodes( codes, n = 2):

    minLengths = []

    for code in codes:

        minLength = input( code, n)
        minLengths.append( minLength[-1] )

    return minLengths


def computeResult( codes, lengths):

    result = 0

    for code, length in zip( codes, lengths):

        code = "".join( d for d in code if d.isdigit() )
        code = int( code )

        result += code * length

    return result


def decode( code ):

    result = Counter()

    for ii in range( len(code) - 1 ):

        subcode = code[ ii:ii+2 ]
        key = mappings[ subcode ]

        result[ key ] += 1
    
    return result


def decodeCounter( codeCounter ):

    result = Counter()

    for code in codeCounter:

        n = len( code )
        nCases = codeCounter[ code ]

        code = "A" + code

        for ii in range( n ):
            key = mappings[ code[ii:ii+2] ]
            result[ key ] += nCases

    return result


def checkCodesPart2( codes, n):

    minLens = []

    for code in codes:
        code = "A" + code

        instructionLength = 0
        result = decode( code )

        for __ in range( n - 1 ):
            result = decodeCounter( result )

        result = decodeCounter( result )

        instructionLength = [ result[key] * (len( key )) for key in result ]
        instructionLength = sum( instructionLength )

        minLens.append( instructionLength )

    return minLens

            

        