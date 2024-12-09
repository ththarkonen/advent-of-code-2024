import diskdf
from copy import deepcopy

file = open("./day9/test.txt")
line = file.readlines()

disk = diskdf.parse( line )
defragmentedDisk = diskdf.defragment( deepcopy( disk ) )
defragmentedDiskFiles = diskdf.moveFiles( deepcopy( disk ) )

checksum = diskdf.computeChecksum( defragmentedDisk )
checksumFiles = diskdf.computeChecksum( defragmentedDiskFiles )

print( checksum )
print( checksumFiles )