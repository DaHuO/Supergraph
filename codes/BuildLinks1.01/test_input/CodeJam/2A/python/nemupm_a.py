from collections import Counter

T = input()

converter = {}
converter[1] = {"P":1, "R":2, "S": 3}
tmp = {2: 1, 3: 2, 6: 3}
for i in xrange(2, 14):
	converter[i] = {
		"P": tmp[converter[i-1]["P"]*converter[i-1]["R"]],
		"R": tmp[converter[i-1]["R"]*converter[i-1]["S"]],
		"S": tmp[converter[i-1]["P"]*converter[i-1]["S"]]
	}
converter2 = {
	"P": "PR",
	"R": "RS",
	"S": "PS"
}

for i in xrange(T):
	N, R, P, S = map(int,raw_input().split())
	answers = []
	for seed in ["P","R","S"]:
		ans = seed
		for ii in xrange(N, 0, -1):
			tmp = ""
			for char in ans:
				t = converter2[char]
				if converter[ii][t[0]] > converter[ii][t[1]]:
					t = t[1] + t[0]
				tmp += t
			ans = tmp
		counter = Counter(ans)
		if counter["P"] == P and counter["R"] == R and counter["S"] == S:
			answers.append(ans)
	if len(answers) == 0:
		print "Case #%d: IMPOSSIBLE"  % (i+1)
	else:
		print "Case #%d: %s"  % (i+1, min(answers))