#!/usr/bin/python3
import sys

file_prefix = 'B-small-attempt0'

filein = open(file_prefix + '.in')
fileout = sys.stdout if 'sample' in file_prefix else open(file_prefix + '.out', 'w')
linein = lambda: filein.readline().strip()
lineout = lambda s: fileout.write(s + '\n')

ncases = int(linein())
'''
def areDifferentAxis(a, b):
	smaller = 0
	larger = 0
	for i in range(len(a)):
		if a[i] == b[i]:
			return True
		elif a[i] < b[i]:
			smaller += 1
		else:
			larger += 1
	if smaller != 0 and larger != 0:
		return True
	return False

def areSwapped(optA, optB, i):
	if areDifferentAxis(opt[0], nextOpt[0], i):
		return True
	elif len(optA) == 2 and areDifferentAxis(optA[1], optB[0], i):
		return False
	elif len(optB) == 2 and areDifferentAxis(optA[0], optB[1], i):
		return False
	elif len(optA) == 2 and len(optB) == 2 and areDifferentAxis(optA[1], optB[1], i):
		return True
	return None
	'''

for case in range(ncases):
	N = int(linein())

	sheets = []
	for i in range(N*2 - 1):
		sheets.append([int(x) for x in linein().split()])

	options = []
	for i in range(N):
		minVal = min(sheet[i] for sheet in sheets)
		opt = []
		for sheet in list(sheets):
			if sheet[i] == minVal:
				sheets.remove(sheet)
				opt.append(sheet)
		options.append(opt)

	print(options)

	'''
	nextIsSwapped = []

	for i in range(N-1):
		opt = options[i]
		nextOpt = options[i + 1]
		nextIsSwapped.append(areSwapped(opt, nextOpt, i))

	print(nextIsSwapped)
	'''

	def dimIsOK(col, choices, rowDim):
		depth = len(choices)
		if col is None:
			return True

		for (i, choice) in enumerate(choices):
			row = choice[rowDim]
			if row is None:
				continue
			if col[i] != row[depth]:
				return False
		return True

	def tryPosition(choices):
		if len(choices) > 0:
			curChoice = choices[-1]
			prevChoices = choices[:-1]
			if not dimIsOK(curChoice[0], prevChoices, 1):
				return None
			elif not dimIsOK(curChoice[1], prevChoices, 0):
				return None

		if len(choices) == N:
			return choices

		nextOption = options[len(choices)]
		single = len(nextOption) == 1

		if single: trials = [(nextOption[0], None), (None, nextOption[0])]
		else: trials = [(nextOption[0], nextOption[1]), (nextOption[1], nextOption[0])]

		for t in trials:
			x = tryPosition(choices + [t])
			if x is not None: return x

		return None

	answer = tryPosition([])
	print(answer)
	for i, c in enumerate(answer):
		if c[0] is None:
			colDim = 1
			row = i
		elif c[1] is None:
			colDim = 0
			row = i

	print (colDim, row)
	result = []
	for c in answer:
		result.append(str(c[colDim][row]))

	lineout("Case #{0}: {1}".format(case + 1, ' '.join(result)))
