# -*- coding: utf-8 -*-
from sys import stdin
t = int(input())
for case in range(t):
	n = int(input())
	i = 0
	digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	while n > 0 and len(digits) > 0:
		i +=1
		s = list(map(int, str(n * i )))
		for j in s:
		    digits.discard(j)
	sheep = open('out.out', 'a')
	if n*i  <= 0:
		print("Case #%d: %s" %(case+1 , ("INSOMNIA")))
	else:
		print("Case #%d: %s" %(case+1 , (n*i)))

