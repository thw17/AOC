from __future__ import print_function
import collections
import sys


def check_room(input_string):
	"""
	"""
	name = ""
	sector = ""
	checksum = ""
	if input_string == "":
		return (False, 0)
	for idx, i in enumerate(input_string):
		if i.isalpha():
			name += i
		elif i.isdigit():
			sector += i
		elif i == "[":
			check_start = idx
			break
	for i in input_string[check_start:]:
		if i not in ["[", "]"]:
			checksum += i

	print(name)
	print(sector)
	print(checksum)
	top_five = ""
	mc = collections.Counter(name).most_common()
	print(mc)
	try:
		if mc[4][1] == mc[5][1]:
			equal = [x[0] for x in mc if x[1] == mc[4][1]]
			equal.sort()

			for i in mc:
				if i[1] > mc[4][1]:
					top_five += i[0]
			index = 0
			while len(top_five) < 5:
				top_five += equal[index]
				index += 1
		else:
			top_five = "".join([str(x[0]) for x in mc[:5]])
			print(top_five)
	except:
		top_five = "".join([str(x[0]) for x in mc[:5]])
		print(top_five)

	if top_five == checksum:
		real = True
	else:
		real = False

	return (real, int(sector))

if __name__ == "__main__":
	input_file = sys.argv[-1]

	total = 0
	with open(input_file, "r") as f:
		for line in f:
			room_info = check_room(line.strip())
			if room_info[0] is True:
				total += room_info[1]

	print(total)
