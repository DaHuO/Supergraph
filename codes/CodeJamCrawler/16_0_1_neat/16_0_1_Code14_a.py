#! /usr/bin/env python3
'''
' Title:	Google Code Jam 2016 - A. Counting Sheep
' Author:	Cheng-Shih, Wong
' Date:		2016/04/09
'''

T = int(input())

for ti in range(1,T+1):
	N = int(input())
	print('Case #%d: '%ti, end='')

	if N==0: print('INSOMNIA')
	else:
		vis = set()

		i = 0
		while len(vis)<10:
			i += 1
			val = str(i*N)
			vis |= set([c for c in val])

		print(i*N)
