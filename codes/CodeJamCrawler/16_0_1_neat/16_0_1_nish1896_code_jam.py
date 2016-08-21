
t = int(input().strip())
num =[]
output=[]
seen_digit=[]


for i in range(10):
	seen_digit.append(False)

seen_digit1=tuple(seen_digit)
# print(seen_digit1)

def find_next_num(N,seen_digit,pos):
	factor=1
	# seen_digit= seen_digit1
	if N=='0':
		return "Case #"+str(pos+1)+": INSOMNIA"
	else:
		while not all(element for element in seen_digit):
			for i in str(factor*int(N)):
				seen_digit[int(i)]=True
			factor = factor+1
	return "Case #"+str(pos+1)+": "+ str((factor-1)*int(N))			


for i in range(t):
	num.append(input().strip())
	output.append(find_next_num(num[i],seen_digit,i))
	# print(seen_digit1)
	seen_digit=list(seen_digit1)

	# print(seen_digit)
	# print(output[i])

for out in output:
	print(out)


