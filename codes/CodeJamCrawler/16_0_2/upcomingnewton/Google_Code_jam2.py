import sys

def find_sol(x):
	if x.find('-') == -1: # all +
		return 0
	if x.find('+') == -1: # all -
		return 1
	last_index = x.rfind('+-')
	if last_index != -1:
		# convert x[:last_index] to +
		# then you have ++++++++-
		# then convert all initial +++ to --- then convert all -- to +++
		ans = find_sol(x[:last_index])
		return ans + 2
	elif x.find("-+") != -1:
		idx = x.find("-+")
		if idx == 0:
			return 1
		else:
		# convert everything before idx to --
			return find_sol(x[:idx])
	return 0

data = [x.strip() for x in sys.stdin.readlines()]
n = int(data[0])
data = data[1:]
for (i,x) in enumerate(data):
	ans = 0
	if x.find('-') != -1:
		if x.find('+') == -1:
			ans = 1
		else:
			ans = find_sol(x)
	print "Case #{0}: {1}".format(i+1,ans)