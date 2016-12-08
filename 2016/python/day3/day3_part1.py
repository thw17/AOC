from __future__ import print_function
import sys


def test_triangle(dim):
	"""
	Tests if dimensions can come from a triangle.

	dim is a list of the three dimensions (integers)
	"""
	dim = [int(x) for x in dim]
	dim.sort()
	if dim[0] + dim[1] > dim[2]:
		return True
	else:
		return False


if __name__ == "__main__":
	input_file = sys.argv[-1]

	passing = 0
	with open(input_file, "r") as f:
		for i in f:
			k = i.strip()
			if test_triangle(k.split()) is True:
				passing += 1

	print("{} listed triangles are possible".format(passing))
