
def parse( lines ):

    connections = {}

    for line in lines:

        line = line.replace("\n","")
        line = line.split("-")

        A = line[0]
        B = line[1]

        if A not in connections:
            connections[A] = [B]
        if B not in connections:
            connections[B] = [A]
        if A in connections and B not in connections[A]:
            connections[A].append( B )
        if B in connections and A not in connections[B]:
            connections[B].append( A )

    return connections


def getLoops( connections ):

    loops = set()

    for initialConnection in connections:
        for subconnection in connections[ initialConnection ]:
            for subsubconnection in connections[ subconnection ]:
                for connection in connections[subsubconnection]:

                    loop = [ initialConnection, subconnection, subsubconnection]
                    loop.sort()
                    loop = tuple( loop )
                    if connection == initialConnection and len( set(loop) ) == 3:
                        loops.add( loop )

    return loops


def filterLoops( loops ):

    validLoops = []

    for loop in loops:
        for port in loop:
            if port[0] == "t":
                validLoops.append( loop )
                break

    return validLoops


def findNetworks( loops, connections):

    networks = []

    for ii, startingLoop in enumerate( loops ):
        
        print( (ii+1) / len(loops) )

        network = {}
        network["nodes"] = startingLoop
        network["loops"] = [ startingLoop ]

        for loop in loops:
            if loop == startingLoop: continue

            loop = set( loop )
            notDense = False

            for ii, networkLoop in enumerate( network["loops"] ):

                networkLoop = set( networkLoop )
                nodeSet = set( network["nodes"] )
                
                if ii == 0:
                    intersect = networkLoop.intersection( loop )
                    newNode = loop.difference( nodeSet )
                else:
                    intersect = networkLoop.intersection( loop, intersect)
                    newNode = newNode.union( loop.difference( nodeSet ) )

                if len( intersect ) != 2 and len( newNode ) != 1:
                    notDense = True
                    break

            if notDense: continue

            for node in newNode:
                ports = connections[ node ]

            for port in network["nodes"]:
                if port not in ports:
                    notDense = True
                
            if notDense: continue

            network["nodes"] += ( node, )
            network["loops"].append( loop )

        network["nodes"] = sorted( network["nodes"] )
        networks.append( network )

    return networks


def getLargestNetwork( networks ):

    networkLengths = [ len( network["nodes"] ) for network in networks]
    maxLength = max( networkLengths )

    for network in networks:
        if len( network["nodes"] ) == maxLength:
            result = ",".join( network["nodes"] )
            break

    return result




            

            





