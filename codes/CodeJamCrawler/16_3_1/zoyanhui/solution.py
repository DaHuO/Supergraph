def print_case_result(case_num, result):
    print "Case #" + str(case_num) +": " + str(result)



def solution(senators, total, N):
	result = []
	while total > 0:
		senators.sort(reverse=True)
		if senators[1][0] <= (total-2) /2:
			result.append(senators[0][1] + senators[0][1])
			senators[0][0] -= 2
			total -= 2
		elif N > 2 and senators[1][0] > 0 and senators[2][0] <= (total-2) /2:
			result.append(senators[0][1] + senators[1][1])
			senators[0][0] -= 1
			senators[1][0] -= 1
			total -= 2
		elif N == 2 and senators[1][0] > 0:
			result.append(senators[0][1] + senators[1][1])
			senators[0][0] -= 1
			senators[1][0] -= 1
			total -= 2
		else:
			result.append(senators[0][1])
			senators[0][0] -= 1
			total -= 1
	return ' '.join(result)



if __name__ == '__main__':
    testcase_num = int(raw_input())
    for case_num in range(1, testcase_num+1):
        N = int(raw_input())
        inputs = [int(x) for x in raw_input().split()]
        i = 0
        senators = []
        total = 0
        for senator_num in inputs:
        	senators.append([senator_num, chr(ord('A') + i)])
        	i+=1
        	total += senator_num
        print_case_result(case_num, solution(senators, total, N))
