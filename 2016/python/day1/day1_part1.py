"""
Quick and inelegant brute force approach to Day 1 Part 1 of AOC 2016

How far is the shortest path to your destination, assuming you can only walk
on the street grid of the city?

You land facing north and follow sequences, turning left or right for a given
number of blocks.  E.g.,

R2, L3 will leave you 2 blocks east and 3 blocks north, or 5 blocks away
R2, R2, R2 leaves you 2 blocks due South of your starting position,
	or 5 blocks away
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

	position = ("north", 0, 0)
	for i in in_list:
		position = new_position(position, i)

	print("The Easter Bunny HQ is {} blocks away".format(
		abs(position[1]) + abs(position[2])))
