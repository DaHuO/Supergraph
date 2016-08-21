#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

myfile = open("A-large.in.txt", "r")
content=myfile.read().splitlines()
myfile.close()

num_cases = content[0]
numbers = content[1:]
l = 0

def check(c,t):
	t = list(map(int, str(t)))

	for i in t:
		if i not in lnum:
			lnum.append(int(i))
			c += 1

	return c


outfile = open('texto.txt', 'w')
for k in numbers:
	N=k

	l += 1
	if N == "0":
		outfile.write("Case #" + str(l) + ": INSOMNIA"+ "\n")

	else:
		counter = 0
		i = 1
		lnum = []
		#n = 1
		while counter != 10:
			t= int(N) * i
			counter = check(counter,t)
			i += 1

		outfile.write("Case #" + str(l) + ": " + str(t)+ "\n")

