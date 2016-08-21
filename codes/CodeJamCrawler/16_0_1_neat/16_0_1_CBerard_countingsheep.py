### google code jam 2016 qualifier problem A
import numpy as np 
import sys

def count(num):
	# takes number n and decomposes it into digits
	# special case when n=0
	n=int(num) #convert to integer
	nstring=str(n) # convert to string
	nlen=len(nstring) # get number of digits
	numlist=list(nstring)
	digitlist=["0","1","2","3","4","5","6","7","8","9"] # list of digits Bleatrix wants to see

	### handle 0 case
	# print insomnia if first digit is 0
	# note when "04" converted to integer it will be "4"
	# so 04,05, etc remains valid input with this method
	if (numlist[0] == "0"):
		return "INSOMNIA"

	# the bulk of the function
	nstart = n
	itercount = 1 #start counter (how many numbers must she count?)
	i=0
	while digitlist != []:
		nstartdigits=list(str(nstart))
		nstartlen = len(str(nstart))
		for j in range(nstartlen):
			# check if digit in numbersseen list
			# if yes, delete element from numbersseen
			if (nstartdigits[j] in digitlist):
				digitlist.remove(nstartdigits[j])
				# check if list empty; if so return current count
				if (digitlist==[]):
					#print numbersseen

					return nstart
		# all digits have been removed from numbersseen this iteration
		itercount+=1
		i+=1
		nstart = n*(i+1) 

	return nstart

inputs=np.loadtxt("./Inputcountsheep.txt",skiprows=0,unpack=True)
numtests=int(inputs[0])
numbers=inputs[1:]
answers=[]
for number in numbers:
	answers.append(count(number))
	#print number, count(number)


#### write
fout=open("./count_out.txt","w")
casenum=1
#fout.write("Input	Output \n")
for k in range(numtests):

	#if k==0:
	fout.write("Case #"+str(k+1)+": "+str(answers[k])+"\n")
	#elif k==(numtests):
	#	fout.write(str(int(numbers[k-1]))+"\n")
	#else:
	#	fout.write(str(int(numbers[k-1]))+"	Case#"+str(k+1)+": "+str(answers[k])+"\n")

fout.close()




