with open("t1.in") as f:
	content = f.readlines()

A = ord('A')

T = int(content[0])
content = content[1:]
case = 0


def takeOthers(parties, length, curr_ind, max_first):
	if curr_ind >= length:
			return "", curr_ind
	while curr_ind == max_first or parties[curr_ind] == 0:
		curr_ind += 1
		if curr_ind >= length:
			return "", curr_ind

	# Remove
	parties[curr_ind] -= 1
	# Add to string	
	return chr(A+curr_ind), curr_ind

def takeMax(max, ind):
	return chr(A+ind) 

for i in range(T):
	case += 1
	
	N = int(content[2*i])
	parties = [int(n) for n in content[2*i+1].split()]

	# Max num of sentaors of a party
	max_first = 0
	sum_all = 0
	for j in range(len(parties)):
		sen_num = parties[j]
		sum_all += sen_num 
		if sen_num > parties[max_first]:
			max_first = j

	max_part = parties[max_first]
	sum_others = sum_all - max_part

	curr_ind = 0
	string = ""
	length = len(parties)

	while sum_others+max_part > 0:
		string += " "
		if sum_others >= max_part+2:
			#print(111, sum_others, max_part)
			# Remove from others 2 person
			s, curr_ind = takeOthers(parties, length, curr_ind, max_first)
			s2, curr_ind = takeOthers(parties, length, curr_ind, max_first)

			string += s+s2

			sum_others -= 2

		elif sum_others == max_part+1:
			#print(222, sum_others, max_part)
			# tako one from others
			s, curr_ind = takeOthers(parties, length, curr_ind, max_first)
			string += s
			sum_others -= 1

		elif sum_others == max_part:
			#print(333, sum_others, max_part)
			# tako one from others
			s, curr_ind = takeOthers(parties, length, curr_ind, max_first)
			string += s
			# take one from max
			string += takeMax(max_part, max_first)
			
			sum_others -= 1
			max_part -= 1

	print("Case #"+str(case)+":" + string)