def count(n):
	n = int(n)
	numList = [0,1,2,3,4,5,6,7,8,9]
	ant = 10
	currentNumber = 0
	if n == 0:
		return n
	while ant != 0:
		currentNumber += n
		for i in str(currentNumber):
			for j in numList:
				if int(i) == j:
					numList[int(i)] = -1
					ant -= 1

	answer = currentNumber
	return answer

def main():
    fil = open('input.txt','r')
    output = open('output.txt','w')
    cases = fil.readline()
    for i in range(int(cases)):
        tallet = fil.readline()
        svaret = count(tallet)
        if svaret == 0:
        	print("Case #"+str(i+1)+": INSOMNIA")
        	output.write("Case #"+str(i+1)+": INSOMNIA"+"\n")
    	else:
        	print("Case #"+str(i+1)+": "+str(svaret))
        	output.write("Case #"+str(i+1)+": "+str(svaret)+"\n")
    output.close()
    fil.close()

main()