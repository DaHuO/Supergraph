import time
glob = [0,1,2,3,4,5,6,7,8,9]
f = open("A-large.in", "r")

content = f.read()

list = content.split("\n")

f2 = open("out2.in", "w")

t = int(list[0])


for i in range (1, t+1):
	temp = int(list[i])
	mult = 0
	digits = []
	flag = 0
	print("starttttttttttttttttttttt")
	print(temp)

	if temp == 0:
		result = "INSOMNIA"
	else:

		while flag == 0:
			mult = mult +1
			curr = temp*mult
			print(curr)
			# time.sleep(1)
			curr2 = str(curr)
			for k in range(0, len(curr2)):
				# print("starttttttttttttttttttttt")
				if int(curr2[k]) not in digits:
					# print("adding thisss" + curr2[i])
					digits.append(int(curr2[k]))
					# print(digits)
					# print(glob)
					# print(set(glob) == set(digits))

					result = curr2
					if(set(glob) == set(digits)):
						print("fhgggggggggg")
						flag = 10
				# break


	f2.write("Case #{}: {}\n".format(i, result))


