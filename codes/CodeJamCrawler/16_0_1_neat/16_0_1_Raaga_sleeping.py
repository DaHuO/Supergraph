filename = "A-large.in.txt"
f = open("outputlarge.txt","w")

with open(filename) as fn:
	content = fn.readlines()

print "Total Cases:" , content[0]
x="h"
for i in range(1, len(content)):
	N = content[i]
	allCombo = 1
	j=1
	num=0
	one=0
	two=0
	three=0
	four=0
	five=0
	six=0
	seven=0
	eight=0
	nine=0
	zero=0
	while (allCombo==1):
		num = int(N) * j
		j += 1

		if '1' in str(num):
			one=1
		if '2' in str(num):
			two=1
		if '3' in str(num):
			three=1
		if '4' in str(num):
			four=1
		if '5' in str(num):
			five=1
		if '6' in str(num):
			six=1
		if '7' in str(num):
			seven=1
		if '8' in str(num):
			eight=1
		if '9' in str(num):
			nine=1
		if '0' in str(num):
			zero=1


		if(one and two and three and four and five and six and seven and eight and nine and zero):
			allCombo =0
		if num ==0:
			num ='INSOMNIA'
			allCombo=0
	
	# print "Number:" , N
	# print "Max number for sleeping", str(num)
	# print "Multiplier j:", j
	# x = str(raw_input("press enter to continue:"))
	print "Case #%d: %s" % (i,str(num))
	f.write("Case #%d: %s" % (i,str(num)))
	f.write("\n")
f.close()
