import re

def printCase(num,result):
	return ("Case #%d: " % num) + str(result)
	#return ("Case #{}: {}").format(num,result)

def sleep(num):
	sleepy = True
	for i in range(0,10):
		if not (re.search(str(i), str(num))):
			sleepy = False
	return sleepy;

def getNumbers(num):
	if num == 0:
		return "INSOMNIA"
	counter = 1
	nums = ""
	while True:
		nums = nums + str(num*counter)
		counter  = counter+1
		if sleep(nums) == True:
			break
	return (counter-1)*num;


if __name__ == "__main__":
        import fileinput
        f = fileinput.input()
        T = int(f.readline())
        for case in range(1, T+1):
                N = int(f.readline())
                print(printCase(case,getNumbers(N)))
