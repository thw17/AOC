"""
AOC 2017 Day 1 Part 1: Inverse Captcha

Review a sequence of digits and find the sum of all digits that match the next
digit in the list. *The digit after the last digit is the first digit*

E.g.:

1122 produces 3
1111 produces 4
1234 produces 0
91212129 produces 9

"""
from __future__ import print_function
import sys


def main():
	input_file = sys.argv[-1]

	with open(input_file, "r") as f:
		in_string = f.read().replace("\n", "")

	result_list = []
	first_digit = in_string[0]
	last_digit = in_string[-1]
	last_seen = first_digit
	for i in in_string[1:]:
		if i == last_seen:
			result_list.append(i)
		last_seen = i
	if first_digit == last_digit:
		result_list.append(first_digit)

	print(
		"Input sequence was: {}. Result is: {}".format(
			in_string, sum(
				[int(x) for x in result_list])))


if __name__ == "__main__":
	main()
