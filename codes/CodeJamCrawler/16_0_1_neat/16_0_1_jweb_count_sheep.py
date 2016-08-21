#!/usr/bin/python
for tc in xrange(1, input() + 1):
	N = input()
	prev_n = -1
	curr_n = -1
	check = [ False, False, False, False, False, False, False, False, False, False ]
	checked_cnt = 0
	multi = 1
	while True:
		curr_n = N * multi
		if curr_n == prev_n:
			print "Case #%d: INSOMNIA" % (tc)
			break
		prev_n = curr_n
		str_n = str(curr_n)
		for ch in str_n:
			if not check[int(ch)]:
				check[int(ch)] = True
				checked_cnt += 1
		if checked_cnt == 10:
			print "Case #%d: %d" % (tc, curr_n)
			break
		multi += 1
