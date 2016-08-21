#!/usr/bin/python

import sys;

T = int(raw_input());

for i in range(T):

	N = int(raw_input());

	if N != 0:

		master = set(range(10));
		multiplier = 0;

		while 0 != len(master):

			multiplier += 1;
			considerable = multiplier*N;

			while considerable > 0:
				master.discard(considerable%10);
				considerable /= 10;
		print("Case #%d: %d" %(i+1, multiplier*N) );
	else:
		print("Case #%d: INSOMNIA" %(i+1));
