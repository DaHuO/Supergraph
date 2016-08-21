f = open("B-large.in", "r")
new_file = open("revengePancakesLargeSol", "w")
t = int(f.readline())

def amount_switches(pancakes_happiness):
	# print len(pancakes_happiness)
	current_sign = "+"
	counter = 0
	if pancakes_happiness[0] == "+":
		counter += 1
	if pancakes_happiness[-1] == "+":
		counter -= 1
	for i in pancakes_happiness:
		if i != current_sign:
			current_sign = i
			counter += 1
	return counter

# print amount_switches('+++')
for i in range(1,t+1):
	pancakes_happiness = f.readline()[:-1]
	# print pancakes_happiness
	# print amount_switches(pancakes_happiness)
	# print list(pancakes_happiness)
	new_file.write("Case #"+str(i)+ ": "+str(amount_switches(pancakes_happiness))+"\n")
