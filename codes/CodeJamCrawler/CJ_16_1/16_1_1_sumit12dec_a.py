N = input()

test_cases = []
results = []
for i in range(0, N):
	test_cases.append(raw_input())



def get_output(string):
	listing = [string[0]] 
	first_letter = string[0]
	L = len(string)
	for i in range(1, len(string)):
		new_listing = listing[:]
		for each in new_listing:
			listing.append(each + string[i])
			listing.append(string[i] + each)
	temp = filter(lambda x:len(x)==L, listing)
	temp.sort()
	return temp[-1]


for each_string in test_cases:
	results.append(get_output(each_string))

for i in range(0, len(results)):
	print "Case #{0}: {1}".format(i+1, results[i])
