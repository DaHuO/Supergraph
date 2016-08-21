def solve(N):
	if N == 0:
		return 'INSOMNIA'

	numbers = '0123456789'
	seen = ''
	i = 0

	while seen != numbers:
		i+=1
		for d in list(str(i*N)):
			if d not in seen:
				seen += d
		seen = ''.join(sorted(seen))
	return i*N

Test = [
0,
1,
2,
11,
1692,
412910,
20,
8,
590388,
212958,
976147,
166,
263599,
929350,
68609,
705674,
714506,
123977,
476345,
242825,
999991,
644346,
472989,
361660,
394253,
9,
416537,
969615,
576830,
717855,
34,
999993,
280545,
548702,
25,
286565,
404368,
124,
639217,
867117,
999998,
10,
50068,
601091,
579484,
1000000,
135359,
999992,
6,
999997,
999995,
778391,
324999,
677643,
999999,
38725,
792404,
207268,
999996,
145205,
564038,
148619,
585414,
246262,
565572,
805448,
250487,
451786,
40,
53424,
389730,
491918,
671813,
125,
200,
864140,
208250,
4,
629132,
784642,
887443,
65229,
3,
7,
269501,
19418,
999994,
961312,
917725,
68017,
552173,
582253,
810974,
12500,
778785,
1250,
436064,
5,
121394,
125000
]

i = 0
for n in Test:
	i+=1
	print('Case #{0}:'.format(i), solve(n))