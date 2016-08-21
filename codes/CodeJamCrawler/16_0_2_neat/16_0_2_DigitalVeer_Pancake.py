def flip(str):
  return str.replace("+","1").replace("-","+").replace("1","-")

def result(num,res):
	return ("Case #%d: " % num) + str(res)

def makeAllHappy(str):
	length = len(str)
	currentStr = str
	flips = 0
	for i in range(length,-1,-1):
		char = currentStr[i-1]
		if (char == "-"):
			currentStr = flip(currentStr)
			flips = flips + 1
	return flips


if __name__ == "__main__":
        import fileinput
        f = fileinput.input()
        T = int(f.readline())
        for case in range(1, T+1):
                S = f.readline()
                print(result(case, makeAllHappy(S)))
