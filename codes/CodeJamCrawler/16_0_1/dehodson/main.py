input_ = open("A-large.in")
output = open("output", 'w')

cases = input_.read().split()

for i in range(0, int(cases[0])):
	not_seen = ['0','1','2','3','4','5','6','7','8','9']
	case_no  = i + 1
	case     = int(cases[case_no])
	result   = ""

	done = 0
	inc = 0
	current = 0

	if(case == 0):
		result = "INSOMNIA"
	else:
		while done == 0:
			inc = inc + 1
			current = case * inc
			for ch in str(current):
				if ch in not_seen:
					not_seen.remove(ch)
			if(not_seen == []):
				done = 1
				result = str(current)

	output.write("Case #"+str(case_no)+": "+result+"\n")

output.close()