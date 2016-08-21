import sys

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().strip()
    result = ""
    ### start
    if line is "0":
    	result = "INSOMNIA"
    else:
    	check = list()
    	num = 1
    	while len(check)<10:
    		N = str(int(line)*num)
    		line_list = list(N)
    		for l in line_list:
    			if l not in check:
    				check.append(l)
    		num += 1
    	result = N

    print("Case #" + str(testCase) + ": " + result)