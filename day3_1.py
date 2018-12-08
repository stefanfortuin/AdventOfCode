# regex: #(\d+) @ (\d+),(\d+): (\d+)x(\d+)

import re

regex = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
length = 1000
claims = [[[]for i in range(length)] for j in range(length)]
totalX = 0

with open("./Input/day3.txt") as f:
    for line in f:
        match = re.match(regex, line)
        
        number = int(match.group(1))
        posX = int(match.group(2))
        posY = int(match.group(3))
        widthX = int(match.group(4))
        widthY = int(match.group(5))

        for x in range(widthX):
            for y in range(widthY):
                if str(claims[posX + x][posY + y]).isdigit():
                    claims[posX + x][posY + y] = 'X'
                    totalX += 1
                elif claims[posX + x][posY + y] != 'X':
                    claims[posX + x][posY + y] = number
        
print(totalX)


