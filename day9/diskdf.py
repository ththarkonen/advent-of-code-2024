
def parse( line ):

    disk = {}
    freeSpace = False
    id = 0

    for c in line[0]:
        c = int( c )

        if freeSpace:
            [ disk[id].append( None ) for _ in range(c) ]
            id = id + 1
        else:
            disk[ id ] = [ id for _ in range(c) ]

        freeSpace = not freeSpace

    return disk


def defragment( disk ):

    defragmented = False

    diskIDs = disk.keys()
    diskIDs = list( diskIDs )

    for id in diskIDs:
        while None in disk[id]:
            
            maxID = max( disk )

            source = disk[ maxID ]
            target = disk[ id ]

            if maxID == id:
                defragmented = True
                break

            while maxID in source and None in target:

                noneIndex = target.index( None )
                maxIndex = source.index( maxID )

                target[ noneIndex ] = maxID
                source[ maxIndex ] = None

                if maxID not in source:
                    del disk[maxID]
                    break

        if defragmented: break

    maxID = max( disk )
    lastFile = disk[ maxID ]
    lastFile = [ d for d in lastFile if d is not None]

    return disk


def moveFile( disk, maxID):

    for id in range( maxID ):

        source = disk[ maxID ]
        target = disk[ id ]

        sourceFileSize = sum( [ ii == maxID for ii in source ] )
        targetFreeSize = sum( [ ii == None for ii in target ] )

        if targetFreeSize < sourceFileSize: continue

        while maxID in source and None in target:

            noneIndex = target.index( None )
            maxIndex = source.index( maxID )

            target[ noneIndex ] = maxID
            source[ maxIndex ] = None

    return disk


def moveFiles( disk ):

    diskIDs = list( disk.keys() )

    for id in diskIDs[::-1]:
        if id not in disk: continue

        disk = moveFile( disk, id)

    maxID = max( disk )
    lastFile = disk[ maxID ]
    lastFile = [ d for d in lastFile if d is not None]

    return disk


def computeChecksum( disk ):

    total = 0
    position = 0

    for id in disk:
        for ii in disk[id]:
            
            if ii is not None: total += position * ii
            position += 1

    return total