#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import itertools
import math

def get_fac(n):
	sq = int(math.sqrt(n)) + 1
	if n % 2 == 0:
		return 2
	i = 3
	cnt = 0
	while i <= sq:
		if n % i == 0:
			return i
		cnt = cnt + 1
		if cnt > 1000000:
			return -1
		i = i + 2

	return -1

def get_1s(n):
	cnt = 0
	tmp = int("{0:b}".format(n))
	while tmp > 0:
		if tmp % 2 == 1:
			cnt = cnt + 1
		tmp = tmp / 10
	return cnt
	
if __name__ == '__main__':
	N = 32
	J = 500
	N = N - 1
	i = (1 << N) + 1 # 設定控制變數
	e = (1 << (N + 1))
	f = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	idle = 0
	#print "yo",i,e
	while i < e:
		idle = idle + 1
		#print "yo",i,int("{0:b}".format(i))
		if idle == 100:
			i = i + (1 << 10)
			idle = 0
			continue;
		if int("{0:b}".format(i)) % 2 == 0:
			i = i + 1
			continue;
		
		# check if 1's are even
		if get_1s(i) % 2 == 1:
			i = i + 1
			continue;
		canbe = 1
		
		d = 2
		while d < 11:
			if d % 2 == 1:
				f[d] = 2
				d = d + 1
				continue
			tmp = int("{0:b}".format(i))
			v = 0
			p = 0
			cnt_1 = 0
			while tmp > 0:
				v = v + (d**p) * (tmp % 2)
				if tmp % 2 == 1:
					cnt_1 = cnt_1 + 1
				tmp = tmp / 10
				p = p + 1
			f[d] = get_fac(v)
			if f[d] == -1:
				canbe = 0
				break
			d = d + 1
		if canbe == 0:
			i = i + 1
			continue
		#print v,get_fac(v)
		print int("{0:b}".format(i)),f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10]
		i = i + 1
		J = J - 1
		idle = 0
		if J == 0:
			break;
		
