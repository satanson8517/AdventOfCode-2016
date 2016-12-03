input_ = open('../input/01.txt').read()


directions = [('N', [0, 1]),
			  ('E', [1, 0]),
			  ('S', [0, -1]),
			  ('W', [-1, 0])]
visited = list()


def normalize(i):
	while i >= 4:
		i -= 4
	while i <= -5:
		i += 4
	return i


def multiply(m, l):
	lc = list()
	for item in l:
		lc.append(item * m)
	return lc


def add(l1, l2):
	res = [0, 0]
	res[0] = l1[0] + l2[0]
	res[1] = l1[1] + l2[1]
	return res


def parse(input_s):
	bits = input_s.split(', ')
	pos = [0, 0]
	dir = 0
	for bit in bits:
		if bit[0] == 'R':
			dir += 1
		else:
			dir -= 1

		direction = directions[normalize(dir)][1]
		for k in range(0, int(bit[1:])):
			pos = add(pos, direction)
			# pos = add(pos, multiply(int(bit[1:]), direction))
			if pos not in visited:
				visited.append(pos)
			else:
				print('Visited: ' + str(pos))

	return pos

final_pos = parse(input_)
print(final_pos)

blocks = 0
for item in final_pos:
	blocks += abs(item)
print(blocks)



