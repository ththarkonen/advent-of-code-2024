from collections import Counter

def parse( line ):

    data = [ int(d) for d in line.split(" ") ]
    return Counter( data )


def operate( stone ):

    if stone == 0: return [1]

    stoneStr = str( stone )
    stoneEngravingLength = len( stoneStr )

    if stoneEngravingLength % 2 == 0:

        midPoint = stoneEngravingLength // 2
        
        leftStone  = stoneStr[ 0:midPoint ]
        rightStone = stoneStr[ midPoint: ]

        leftStone  = int( leftStone )
        rightStone = int( rightStone )
        
        return [ leftStone, rightStone]
    
    else: return [ 2024 * stone ]


def blink( stones ):

    nextStones = Counter()

    for stone in stones:

        stoneAmount = stones[ stone ]
        newStones = operate( stone )

        for newStone in newStones:
            nextStones[ newStone ] += stoneAmount
        
    return nextStones