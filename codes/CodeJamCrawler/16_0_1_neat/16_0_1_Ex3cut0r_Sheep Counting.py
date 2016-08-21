# Author: Nathan Landman



def count_all_sheep():
	test_number = int(raw_input())
	for i in xrange(1, test_number+1):
		n = int(raw_input())
		print "Case #"+ str(i)+ ": "+str(sheep_counting(n))

def sheep_counting(n):
	number_table = {}
	i = 0
	n_copy = n
	if n == 0:
		return "INSOMNIA"
	while (len(number_table) < 10):
		i += 1
		n_copy = n * i
		number_table.update(sheep_instance(n_copy, number_table))
	return n_copy


def sheep_instance(n, number_table):
	for i in str(n):
		number_table[i] = 1
	return number_table

count_all_sheep()

# # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# # This is all you need for most Google Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)
#   # check out .format's specification for more formatting options