A = int(raw_input())

for i in range(A):
	Ans = []
	A = sorted(list(raw_input()))
	list1 = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	
	Zero = A.count("Z")
	for z in range(Zero):
		for j in list1[0]:
			A.remove(j)
		Ans.append("0") 

	Six = A.count("X")
	for x in range(Six):
		for j in list1[6]:
			A.remove(j)
		Ans.append("6") 

	Six = A.count("G")
	for x in range(Six):
		for j in list1[8]:
			A.remove(j)
		Ans.append("8")

	Six = A.count("S")
	for x in range(Six):
		for j in list1[7]:
			A.remove(j)
		Ans.append("7") 

	Six = A.count("U")
	for x in range(Six):
		for j in list1[4]:
			A.remove(j)
		Ans.append("4")
 
	Six = A.count("F")
	for x in range(Six):
		for j in list1[5]:
			A.remove(j)
		Ans.append("5")
 
	Six = A.count("W")
	for x in range(Six):
		for j in list1[2]:
			A.remove(j)
		Ans.append("2")
 
	Six = A.count("R")
	for x in range(Six):
		for j in list1[3]:
			A.remove(j)
		Ans.append("3")
 
	Six = A.count("O")
	for x in range(Six):
		for j in list1[1]:
			A.remove(j)
		Ans.append("1") 

	Six = A.count("N")/2
	for x in range(Six):
		for j in list1[9]:
			A.remove(j)
		Ans.append("9")
	Ans.sort()
	Ans = "".join(Ans)

	print("Case #" + str(i+1) +": " + str(Ans)  )

