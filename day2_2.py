lines = []
with open("./Input/day2.txt") as f:
    for line in f:
        lines.append(line)
           
# it = 0
# for line in lines:
#     it += 1
#     print(it)

#     id = {}
#     pos = 0
#     for char in line:
#         id[char] = pos
#         pos += 1
#         for lineToCheck in lines:
#             idToCheck = {}
#             posToCheck = 0
#             for charToCheck in lineToCheck:
#                 idToCheck[charToCheck] = posToCheck

#                 # if id[char] == idToCheck[charToCheck] and char == charToCheck:
#                 #     print

#                 posToCheck += 1
#                 print(idToCheck)
positions = []

for line in lines:
    pos = 0
    for char in line:
        for lineToCheck in lines:
            if len(lineToCheck) <= pos and lineToCheck[pos] != char:
                print(line) 
        
        pos += 1

for id in positions:
    for char in id:
        pos = id[char]




