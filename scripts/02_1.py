KEYPAD = [None,
		  [0, 2, 4, 0],  # 1
		  [0, 3, 5, 1],  # 2
		  [0, 0, 6, 2],  # 3
		  [1, 5, 7, 0],  # 4
		  [2, 6, 8, 4],  # 5
		  [3, 0, 9, 5],  # 6
		  [4, 8, 0, 0],  # 7
		  [5, 9, 0, 4],  # 8
		  [6, 0, 0, 8]]  # 9
MOVES = ['U', 'R', 'D', 'L']
FILENAME = '../input/02.txt'
START = KEYPAD[5]

ciphers = ''

with open(FILENAME) as f:
	pos = START
	while True:
		c = f.read(1)
		if not c or c == '\n':
			ciphers += str(KEYPAD.index(pos))
			if not c:
				break
		else:
			move = MOVES.index(c)
			if pos[move] != 0:
				pos = KEYPAD[pos[move]]

print(ciphers)
