"""
Quick and inelegant brute force approach to Day 1 Part 2 of AOC 2016

Note: this is just building on day 1 part 1, here adding code to determine
the first point crossed twice
"""
from __future__ import print_function
import sys


def new_position(tup, dir):
	"""
	Takes a starting tuple of (start_direction, east_west_loc, north_south_loc)
	and a string with the direction to take (in the form of R or L followed by
	a number - e.g., R2 or L17)

	Returns tuple of (end_direction, east_west_loc, north_south_loc)
	"""
	if tup[0] == "north":
		if dir[0].upper() == "R":
			out_dir = "east"
		elif dir[0].upper() == "L":
			out_dir = "west"
	elif tup[0] == "east":
		if dir[0].upper() == "R":
			out_dir = "south"
		elif dir[0].upper() == "L":
			out_dir = "north"
	elif tup[0] == "south":
		if dir[0].upper() == "R":
			out_dir = "west"
		elif dir[0].upper() == "L":
			out_dir = "east"
	elif tup[0] == "west":
		if dir[0].upper() == "R":
			out_dir = "north"
		elif dir[0].upper() == "L":
			out_dir = "south"

	if out_dir == "north":
		n_s_out = tup[2] + int(dir[1:])
		e_w_out = tup[1]
	elif out_dir == "south":
		n_s_out = tup[2] - int(dir[1:])
		e_w_out = tup[1]
	elif out_dir == "east":
		n_s_out = tup[2]
		e_w_out = tup[1] + int(dir[1:])
	elif out_dir == "west":
		n_s_out = tup[2]
		e_w_out = tup[1] - int(dir[1:])

	return (out_dir, e_w_out, n_s_out)

if __name__ == "__main__":
	input_file = sys.argv[-1]

	with open(input_file, "r") as f:
		in_string = f.read().replace("\n", "")

	in_list = [x.strip() for x in in_string.split(",")]

	visited = []
	first_crossed = None
	position = ("north", 0, 0)
	for i in in_list:
		start = (position[1], position[2])
		position = new_position(position, i)

		if first_crossed is None:
			new = (position[1], position[2])
			x = new[0] - start[0]
			y = new[1] - start[1]

			if x > 0:
				for j in range(start[0] + 1, new[0] + 1):
					if (j, start[1]) in visited:
						first_crossed = (j, start[1])
						break
					else:
						visited.append((j, start[1]))
			elif x < 0:
				for j in range(new[0], start[0]):
					if (j, start[1]) in visited:
						first_crossed = (j, start[1])
						break
					else:
						visited.append((j, start[1]))
			elif y > 0:
				for j in range(start[1] + 1, new[1] + 1):
					if (start[0], j) in visited:
						first_crossed = (start[0], j)
						break
					else:
						visited.append((start[0], j))
			elif y < 0:
				for j in range(new[1], start[1]):
					if (start[0], j) in visited:
						first_crossed = (start[0], j)
						break
					else:
						visited.append((start[0], j))

	print("The Easter Bunny HQ is {} blocks away\n".format(
		abs(position[1]) + abs(position[2])))

	print("We first crossed our tracks at {}, {} blocks away\n".format(
		first_crossed, abs(first_crossed[0]) + abs(first_crossed[1])))
