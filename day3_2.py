# regex: #(\d+) @ (\d+),(\d+): (\d+)x(\d+)

import re
from functools import reduce

regex = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
length = 1000
claims = [[[]for i in range(length)] for j in range(length)]
totalX = 0

definedSquaredNumber = {}

with open("./Input/day3.txt") as f:
    for line in f:
        match = re.match(regex, line)
        
        number = int(match.group(1))
        posX = int(match.group(2))
        posY = int(match.group(3))
        widthX = int(match.group(4))
        widthY = int(match.group(5))

        definedSquaredNumber[number] = widthX * widthY

        for x in range(widthX):
            for y in range(widthY):
                if str(claims[posX + x][posY + y]).isdigit():
                    claims[posX + x][posY + y] = 'X'
                    totalX += 1
                elif claims[posX + x][posY + y] != 'X':
                    claims[posX + x][posY + y] = number

actualSquaredNumber = {}
for x in range(1000):
    for y in range(1000):
        number = claims[x][y]
        if number == [] or number == 'X':
            continue
            
        if number not in actualSquaredNumber :
            actualSquaredNumber[number] = 1
        else:
            actualSquaredNumber[number] += 1

for number in definedSquaredNumber:
    if number in actualSquaredNumber and actualSquaredNumber[number] == definedSquaredNumber[number]:
        print(number)

    
    
# print(totalX)


