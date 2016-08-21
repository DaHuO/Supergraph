import os
import sys


def output_format(string_number,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(string_number)
    output +="\n"
    return output

def unique_digits_in_number(number):
	return list(set(str(number)))

def add_sheep_number_to_count (number,digits_dict):
	n_digits = unique_digits_in_number(number)
	for n in n_digits:
		digits_dict[n] = digits_dict.get(n,0) + 1
	return digits_dict


#f = open("A-large-practice.in",'r')
f = open("A-large.in",'r')
test_cases = int(f.readline())
out = open("results_0_large.txt",'w')
#print unique_digits_in_number(12333333345)

print test_cases
for i in range(test_cases):
    number = int(f.readline())
    #print number
    digits = {}
    index = 1
    if number == 0 :
        result = "INSOMNIA"
    else:
		while(len(digits.keys()) < 10):
			digits = add_sheep_number_to_count(index*number,digits)
			index +=1
		result = (index-1)*number
    #print result	
    output = output_format(result,i)
    out.write(output)

