counter = 0
lines = 0

with open('../input/03.txt') as f:
	for line in f:
		lines += 1
		sides = list()
		sides.append(int(line[0:5].strip()))
		sides.append(int(line[6:10].strip()))
		sides.append(int(line[11:15].strip()))
		if sides[0] + sides[1] > sides[2] and \
			sides[1] + sides[2] > sides[0] and \
			sides[2] + sides[0] > sides[1]:
			counter += 1

print(counter)
print(lines)
