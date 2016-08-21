T = int(raw_input())

for i in range(T):
	string = raw_input()
	plus = len(filter(lambda x : x, string.split("-")))
	minus = len(filter(lambda x : x, string.split("+")))
	ans = plus + minus
	if string[-1] == "+":
		ans -= 1
	print "Case #%d:" % (i+1), ans