from __future__ import print_function
import sys


def keypad(coords):
	"""
	Takes a tuple of coordinates (x,y) and returns corresponding
	keypad number
	"""
	x = coords[0]
	y = coords[1]

	key = [
		["N", "N", 1, "N", "N"],
		["N", 2, 3, 4, "N"],
		[5, 6, 7, 8, 9],
		["N", "A", "B", "C", "N"],
		["N", "N", "D", "N", "N"]]

	return key[x][y]

def move(start, dir):
	"""
	"""
	if dir == "U":
		mv = (-1, 0)
	elif dir == "D":
		mv = (1, 0)
	elif dir == "L":
		mv = (0, -1)
	elif dir == "R":
		mv = (0, 1)
	else:
		print("Direction needs to be U D L or R. Exiting")
		sys.exit(1)

	end = (start[0] + mv[0], start[1] + mv[1])
	if end[0] < 0 or end[0] > 4:
		return start
	elif end[1] < 0 or end[1] > 4:
		return start
	else:
		return end

if __name__ == "__main__":
	input_file = sys.argv[-1]

	with open(input_file, "r") as f:
		directions = [line.strip() for line in f]

	pos = (2, 0)
	code = ""
	for sequence in directions:
		for movement in sequence:
			pos1 = pos
			pos = move(pos, movement)
			if keypad(pos) == "N":
				pos = pos1
		code += str(keypad(pos))

	print(code)
