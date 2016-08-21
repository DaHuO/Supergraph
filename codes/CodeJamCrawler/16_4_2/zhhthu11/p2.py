import sys
import itertools
import math

def mylog(value):
	if (value == 0):
		return -40
	return math.log(value)

def solve():
	[N, K] = [int(x) for x in raw_input().split(" ")]
	prob = [float(x) for x in raw_input().split(" ")]
	# print "N =",str(N), " K =", str(K), " prob =", str(prob)
	best_tie_rate = 0.0
	select_set = set()
	for select in itertools.combinations(prob, K):
		select_set.add(select)
	# print "select_set =" + str(select_set)
	for select in select_set:
		# print "select =", str(select)
		all_say_yes_log, all_say_no_log = 0.0, 0.0
		for say_yes_prob in select:
			# print "say_yes_prob =", str(say_yes_prob)
			all_say_yes_log += mylog(say_yes_prob)
			all_say_no_log  += mylog(1 - say_yes_prob)

		curr_tie_rate = 0.0
		for say_yes in itertools.combinations(select, K / 2):
			# print "say_yes =", str(say_yes)
			curr_say_yes_log, curr_say_no_log = 0.0, 0.0
			for say_yes_prob in say_yes:
				curr_say_yes_log += mylog(say_yes_prob)
				curr_say_no_log  += mylog(1 - say_yes_prob)
			others_say_no_log = all_say_no_log - curr_say_no_log
			curr_tie_log = curr_say_yes_log + others_say_no_log
			curr_tie_rate += math.exp(curr_tie_log)
		
		if curr_tie_rate > best_tie_rate:
			best_tie_rate = curr_tie_rate
	return best_tie_rate

t = int(raw_input())
for i in range(t):
    print "Case #{}: {}".format(i + 1, solve())
