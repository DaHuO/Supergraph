#!/usr/bin/python3
import sys, os, itertools

file_prefix = 'A-' + ['sample', 'small-attempt0', 'large'][1]
filein = open(file_prefix + '.in', 'r')
fileout = sys.stdout if 'sample' in file_prefix else open(file_prefix + '.out', 'w')
linein = lambda: filein.readline().strip()
def lineout(s, *args):
	global fileout
	out = s.format(*args); fileout.write(out + '\n')
	if fileout != sys.stdout: print(out)

ncases = int(linein())

def winner(a, b):
	# print("{} {} ({} {})".format(a, b, a == 'P', b == 'R'))
	if a == 'P' and b == 'S':
		return 'S'
	elif a == 'R' and b == 'S':
		return 'R'
	elif a == 'R' and b == 'P':
		return 'P'
	return None

def pWorks(s):
	# print("trying '{}'".format(s))
	if len(s) == 1: return True
	nextS = ''
	for i in range(len(s) // 2):
		w = winner(s[i*2], s[i*2 + 1]) or winner(s[i*2 + 1], s[i*2])
		# print("{} {} -> {}".format(s[i*2], s[i*2 + 1], w))
		if not w: return False
		nextS += w
	return pWorks(nextS)

for case in range(ncases):
	N, R, P, S = (int(x) for x in linein().split())

	letters = P * 'P' + R * 'R' + S * 'S'

	answer = "IMPOSSIBLE"

	for pl in itertools.permutations(letters):
		p = ''.join(pl)
		if pWorks(p):
			answer = p
			break

	lineout("Case #{0}: {1}", case + 1, answer)
