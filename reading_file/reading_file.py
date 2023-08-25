example = 'test.txt'

file = open(example, 'r')
print(file.name)
print(file.mode)

file_content = file.read()
print(file_content)
print(type(file_content))
file.close()

# Better way to open files

with open(example, 'r') as file_2:
    # Print the first n characters of the file.
    print(file_2.read(4))
    print(file_2.read(4))
    print(file_2.read(7))
    print(file_2.read(15))
    
with open(example, 'r') as file_3:
    print('first line: ' + file_3.readline())

with open(example,"r") as file_3:
    i = 0
    for line in file_3:
        print("Iteration", str(i), ": ", line)
        i = i + 1