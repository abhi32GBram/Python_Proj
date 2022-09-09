# read
# write
# append

# read as a string
# file = open("C:\\temp\\data.txt", 'r')
# lines = file.read()
# print(lines)
# print(type(lines))
# file.close()

# read as a list
# file = open("C:\\temp\\data.txt", 'r')
# lines = file.read().splitlines()
# print(lines)
# print(type(lines))
# file.close()

# list = ["12", "\n", "15.5", "\n", "65.3"]
# file = open("C:\\temp\\data.txt", 'w')
# file.write('Hello')
# file.write('\n')
# file.write('12.75')
# file.writelines(list)
# file.close()

# file = open("C:\\temp\\data.txt", 'a')
# file.write("New Line")
# file.write('\n')
# file.close()

file = open("C:\\temp\\TriData.csv", 'r')
lines = file.read().splitlines()
for line in lines:
    print(line)
    triList = line.split(',')
    print(triList)
    A = (float(triList[0]))
    B = (float(triList[1]))
    H = (float(triList[2]))
    peri = A + B + H
    print('Perimeter = ', peri)
    #print(type(triList[0]))
    #peri = triList[0] + triList[]
file.close()