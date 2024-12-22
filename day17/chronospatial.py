import computer

file = open("./day17/data.txt")
fileContents = file.read()

register, program = computer.parse( fileContents )
output, registerOutput = computer.run( program, register.copy())
print( output )

print("Start part 2. This will take a while.")
input("Press Enter to continue...")
computer.debug( program )
