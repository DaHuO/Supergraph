import os
from sys import *
import re
					

T = int(stdin.readline())
# T = int(stdin.readline())
for t in xrange(T):
	S = list(stdin.readline())
	num = []
	J = []
	# print S
	# S = list(S)
	if '\n' in S:
		S.remove('\n')
	
	# increase speed?
	for l in xrange(len(S)):
		for s in S:
			if s == 'Z':
				num.append(0)
				for i in 'ZERO':
					S.remove(i)	
	for l in xrange(len(S)):
		for s in S:
			if s == 'W':
				num.append(2)
				for i in 'TWO':
					S.remove(i)	
	for l in xrange(len(S)):				
		for s in S:
			if s == 'U':
				num.append(4)
				for i in 'FOUR':
					S.remove(i)		
	# F is already counted in 4
	for l in xrange(len(S)):
		for s in S:
			if s == 'F':
				num.append(5)
				for i in 'FIVE':
					S.remove(i)	
	for l in xrange(len(S)):
		for s in S:
			if s == 'X':
				num.append(6)
				for i in 'SIX':
					S.remove(i)	
	# V is already counted in 5
	for l in xrange(len(S)):
		for s in S:
			if s == 'V':
				num.append(7)
				for i in 'SEVEN':
					S.remove(i)		
	for l in xrange(len(S)):
		for s in S:
			if s == 'G':
				num.append(8)
				for i in 'EIGHT':
					S.remove(i)			
	# T is already counted in 8						
	for l in xrange(len(S)):
		for s in S:
			if s == 'T':
				num.append(3)
				for i in 'THREE':
					S.remove(i)			
	# O is already counted in 2
	for l in xrange(len(S)):
		for s in S:
			if s == 'O':
				num.append(1)
				for i in 'ONE':
					S.remove(i)		
	# O is already counted in 2
	for l in xrange(len(S)):
		for s in S:
			if s == 'O':
				num.append(1)
				for i in 'ONE':
					S.remove(i)
	# E is already counted
	for l in xrange(len(S)):
		for s in S:
			if s == 'E':
				num.append(9)
				for i in 'NINE':
					S.remove(i)				
	# print num
	# print S	
	num = sorted(num)				
	# print num
	# S = []
	print "Case #%d:" %(t+1), "".join(str(x) for x in num)
