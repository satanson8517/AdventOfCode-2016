import numpy

counter = 0
lines = 0
matrix = list()


def process(matr):
	m = numpy.array(matr)
	m = m.transpose()
	count = 0
	for item in m:
		if item[0] + item[1] > item[2] and \
			item[1] + item[2] > item[0] and \
			item[2] + item[0] > item[1]:
				count += 1
	return count

with open('../input/03.txt') as f:
	for line in f:
		lines += 1
		sides = list()
		sides.append(int(line[0:5].strip()))
		sides.append(int(line[6:10].strip()))
		sides.append(int(line[11:15].strip()))
		matrix.append(sides)
		if lines % 3 == 0:
			counter += process(matrix)
			matrix = list()

print(counter)
