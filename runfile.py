from transport import FileParser

file = 'input.txt'
input_file = FileParser.FileParser(file)

print(input_file.simulationTime)
input_file.read_file()