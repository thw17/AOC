# Simply adding to the da3_part1 script

from __future__ import print_function
import sys


def test_triangle(dim):
	"""
	Tests if dimensions can come from a triangle.

	dim is a list or tuple of the three dimensions
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
		while True:
			line1 = f.readline()
			line2 = f.readline()
			line3 = f.readline()

			line1 = line1.strip()
			line2 = line2.strip()
			line3 = line3.strip()

			if line1 == "":
				break

			tri = zip(line1.split(), line2.split(), line3.split())
			for i in tri:
				if test_triangle(i) is True:
					passing += 1

	print(
		"{} listed triangles are possible "
		"(considering rows vertically)".format(passing))
