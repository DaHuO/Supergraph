import sys

name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def flip(pancakes):
	return "".join(list( '-' if i is '+' else '+' for i in pancakes ))

def happy(pancakes, count=1):

	pancakes = pancakes.rstrip('+')

	if pancakes[0] is '+':
		first_minus = pancakes.index('-')
		flippancakes = flip(pancakes[:first_minus][::-1]) + pancakes[first_minus+1:]
	else:
		flippancakes = flip(pancakes[::-1])

	if flippancakes == pancakes:
		return count+1

	if '-' not in flippancakes:
		return count
	else:
		count +=1
		return happy(flippancakes,count)

for testCase in range(1, testCases + 1):
    line = input().rstrip('+')
    result = 0
    ### start
    if len(line) is 0:
    	result = 0
    elif '+' not in line:
    	result = 1
    else:
    	result = happy(pancakes=line)
    	if result == 0:
    		print(line)


    print("Case #" + str(testCase) + ": " + str(result))