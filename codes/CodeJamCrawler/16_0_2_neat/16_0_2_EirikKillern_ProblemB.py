def flip(string):
	array = []
	answer = 0
	for c in string:
		array.append(c)

	for i in range(0,len(array)):
		if array[i] == "-":
			array[i] = False
		else:
			array[i] = True

	while True:
		counter = 1
		for j in range(0,len(array)-1):
			current = (array[0] == False)
			if array[j] == False and array[j+1] == True:
				answer += 1
				for n in range(0,counter+1):
					array[n] = current
			elif array[j] == True and array[j+1] == False:
				answer += 1
				for m in range(0,counter+1):
					array[m] = current
			elif array[j] == array[j+1]:
				counter += 1
		if array[0] != True:
			array=[i==False for i in array]
			answer += 1
		return answer
		
def main():
    fil = open('input.txt','r')
    output = open('output.txt','w')
    cases = fil.readline()
    for i in range(int(cases)):
        seq = fil.readline()
        svaret = flip(seq)
        print "Case #"+str(int(i)+1)+": "+str(svaret)
        output.write("Case #"+str(int(i)+1)+": "+str(svaret)+"\n")
    output.close()
    fil.close()

main()


