import secrets

file = open("./day22/data.txt")
lines = file.readlines()

secretNumbers = secrets.parse( lines )
secretNumbers2000, prices = secrets.iterate( secretNumbers, 2000)
bananas = secrets.getBananas( prices )

total = sum( secretNumbers2000 )
bestBananas = bananas.values()
bestBananas = max( bestBananas )

print( total )
print( bestBananas )
