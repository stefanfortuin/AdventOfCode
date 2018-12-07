twice = 0
thrice = 0

with open("./Input/day2.txt") as f:
    for line in f:
        id = {}
        for char in line:
            if char not in id:
                id[char] = 1
            else:
                id[char] += 1
        
        foundTwice = False
        foundThrice = False
        for char in id:
            if id[char] == 2 and foundTwice is False:
                twice += 1
                foundTwice = True
            if id[char] == 3 and foundThrice is False :
                thrice += 1
                foundThrice = True
            
print(twice)
print(thrice)
answer = twice * thrice
print(answer)


