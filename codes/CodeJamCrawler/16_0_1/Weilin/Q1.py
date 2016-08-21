
def sleep_or_not(N):
	pool = []
	rounds = 1
	while(len(pool) < 10 and rounds < 1000):
		current_num = N * rounds
		series = str(current_num)
		for item in series:
			if item not in pool:
				pool.append(item)
		rounds += 1
	if rounds == 1000:
		return "INSOMNIA"
	else:
		return current_num



#f = open('A-small-attempt3.in')
f = open('A-large.in')
r = f.read()
f.close()
whole_data = r.split('\n')


n = int(whole_data[0])
tests = []
for i in range(n):
	tests.append(long(whole_data[i + 1]))

f_o = open('output.txt', 'w')
for i in range(n): 
	f_o.writelines("Case #" + str(i + 1) + ': ' + str(sleep_or_not(int(tests[i]))) + '\n')
f_o.close()


