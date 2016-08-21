#Nick Robertson

import random
import os
import string
import math

fo = open("foo.txt", "rw+")
fw = open("output.txt", "w")

number_of_tests=int(fo.readline())

for i in range(number_of_tests):
	input= int(fo.readline())
	
	flag = 0
	checkarray = [0] *10
	temp = 0
	repetitions = input * input
	if (repetitions < 1000):
		repetitions = 1000

	if(repetitions>100000):
		repetitions = 100000

	for n in range(1,repetitions):
		temp = n*input;
		
		while (temp>0):
			remainder = temp %10
			temp = int((temp-remainder)/10)
			checkarray[remainder] =1

		count = 0;
		for number in checkarray:
			if(number == 1):
				count +=1
		if count == 10:
			some_string = "Case #{0}: {1}\n".format(i+1, n*input)
			fw.write(some_string)
			flag =1 
			break
		n+=1
	#print checkarray
	if flag ==0:
		some_string  = "Case #{0}: INSOMNIA\n".format(i+1)
		fw.write(some_string)