frequency1 = 0
frequencies = []

with open("./Input/day1.txt") as f:
    for number in f:
        frequency1 += int(number)
        frequencies.append(frequency1)

answer1 = frequency1
print("answer 1: " + str(answer1))

answer2 = 0
frequency2 = 0
frequencies2 = []

while answer2 == 0:
    with open("./Input/day1.txt") as f:
        for number in f:
            frequency2 += int(number)
            
            if frequency2 in frequencies2:
                index = frequencies2.index(frequency2)
                answer2 = frequencies2[index]
                break
            else:
                frequencies2.append(frequency2)

print("answer 2: " + str(answer2))

