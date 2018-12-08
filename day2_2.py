lines = []
with open("./Input/day2.txt") as f:
    for line in f:
        lines.append(line)

for x in lines:
	for y in lines:
		diff = 0
		for i in range(len(line)):
			if x[i] != y[i]:
				diff += 1
		
		if diff == 1:
			ans = ''
			for i in range(len(x)):
				if x[i] == y[i]:
					ans += str(x[i])
			print(ans)
			print(x,y)


