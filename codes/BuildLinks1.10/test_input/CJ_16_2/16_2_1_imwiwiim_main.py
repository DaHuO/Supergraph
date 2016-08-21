
arr =[["ZERO",'Z'],
	["TWO", 'W'],
	["SIX", 'X'],
	["SEVEN", 'S'],
	["FIVE", 'V'],
	["FOUR", 'F'],
	["THREE", 'R'],
	["EIGHT", 'T'],
	["ONE",  'O'],
	["NINE", 'E']]
val = {
	"ZERO": "0",
	"TWO": "2",
	"SIX": "6",
	"SEVEN": "7",
	"FIVE": "5",
	"FOUR": "4",
	"THREE": "3",
	"EIGHT": "8",
	"ONE": "1",
	"NINE": "9",
	
}

def solve (s):
 	ans = []
	for [n,l] in arr:
		while s.find(l) != -1:
			ans.append(val[n])
			for c in n:
				i = s.find(c)
				if i < len(s)-1:
					s = s[0:i] + s[i+1:]
				else:
					s = s[0:-1]
	ans.sort()
	s = ""
	for a in ans:
		s += a
	return s



f = open("A-small-attempt0 (1).in")

T = int(f.readline())
for case in range(1,T+1):
	s = f.readline()
	if s[len(s)-1] == "\n":
		s = s[0:len(s)-1]
	print "Case #{0}: {1}".format(case,solve(s))





