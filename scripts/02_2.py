A = 10
B = 11
C = 12
D = 13
KEYPAD = [None,
		  [0, 0, 3, 0],  # 1
		  [0, 3, 6, 0],  # 2
		  [1, 4, 7, 2],  # 3
		  [0, 0, 8, 3],  # 4
		  [0, 6, 0, 0],  # 5
		  [2, 7, A, 5],  # 6
		  [3, 8, B, 6],  # 7
		  [4, 9, C, 7],  # 8
		  [0, 0, 0, 8],  # 9
		  [6, B, 0, 0],  # A
		  [7, C, D, A],  # B
		  [8, 0, 0, B],  # C
		  [B, 0, 0, 0]]  # D
MOVES = ['U', 'R', 'D', 'L']
FILENAME = '../input/02.txt'
START = KEYPAD[5]

ciphers = ''

with open(FILENAME) as f:
	pos = START
	while True:
		c = f.read(1)
		if not c or c == '\n':
			ciphers += str(hex(KEYPAD.index(pos))).replace("0x", "").capitalize()
			if not c:
				break
		else:
			move = MOVES.index(c)
			if pos[move] != 0:
				pos = KEYPAD[pos[move]]

print(ciphers)
