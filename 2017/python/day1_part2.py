"""
AOC 2017 Day 1 Part 2: Inverse Captcha

Review a sequence of digits and find the sum of all digits that match the digit
halfway through the list. For example, if the list contains 10 items, only
include a digit if the digit (10/2 = 5) 5 steps forward matches it. All lists
will contain an even number of elements.
*The list is circular!*

E.g.:

1212 produces 6
1221 produces 0
12345 produces 4
123123 produces 12
12131415 produces 4

"""
from __future__ import print_function
import sys


def main():
	input_file = sys.argv[-1]

	with open(input_file, "r") as f:
		in_string = f.read().replace("\n", "")

	input_length = len(in_string)
	steps = input_length / 2
	doubled = in_string + in_string
	result_list = []
	for idx, i in enumerate(in_string):
		if i == doubled[idx + steps]:
			result_list.append(i)

	print(
		"Input sequence was: {}. Result is: {}".format(
			in_string, sum(
				[int(x) for x in result_list])))


if __name__ == "__main__":
	main()
