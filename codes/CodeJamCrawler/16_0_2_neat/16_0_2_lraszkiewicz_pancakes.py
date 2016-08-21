def reverseAndNegate(tab):
	tab = tab[::-1]
	for i in range(0, len(tab)):
		if tab[i] == '+':
			tab[i] = '-'
		else:
			tab[i] = '+'
	return tab

def plusEnd(tab, res):
	while tab and tab[-1] == '+':
		tab = tab[:-1]
	return tab, res

def minusBegin(tab, res):
	while tab and tab[0] == '-':
		tab = tab[1:]
	return reverseAndNegate(tab), res+1

def plusBegin(tab, res):
	while tab and tab[0] == '+':
		tab = tab[1:]
	return reverseAndNegate(tab), res+2

tests = int(input())
for case in range(1, tests + 1):
	tab = list(input())
	res = 0
	while tab:
		if tab[-1] == '+':
			tab, res = plusEnd(tab, res)
		elif tab[0] == '-':
			tab, res = minusBegin(tab, res)
		elif tab[0] == '+':
			tab, res = plusBegin(tab, res)
	print("Case #" + str(case) + ": " + str(res))
