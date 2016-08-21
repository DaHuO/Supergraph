
numbers=["0","1","2","3","4","5","6","7","8","9"]
print("Enter test_case")
# test_case= input()

def main(n,x):
	if n==0:
		return "Case #"+str(x)+": INSOMNIA"
	results=[]
	nr=0
	count=1
	while True:
		if len(results)==10:break
		number = n*count
		
		for i in list(str(number)):
			# print n
			if i in numbers and i not in results:
				results.append(i)
		nr= number			
		count+=1
	return "Case #"+str(x)+": "+str(nr)
with open("input.txt") as g:
	next(g)
	i=1

	for line in g:

		if line=="" or line=="\n" or line=="\t":pass
		else:
			with open("output.txt","a") as f:
				
				
				f.write(main(int(line),i)+"\n")
				i+=1
				# print i
# for i in range(test_case):
# 	ins= input()
# 	with open("output.txt","a") as f:
# 		f.write(main(ins,i)+"\n")
# 	# print main(ins,i)
