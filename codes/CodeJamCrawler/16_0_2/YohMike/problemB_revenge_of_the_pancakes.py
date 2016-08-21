import os
import sys


def output_format(string_number,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(string_number)
    output +="\n"
    return output

def are_pancakes_flipped_the_same(pancakes):
	flipped = list(set(pancakes))
	#print flipped
	if len(flipped) == 1:
		return flipped[0]
	else:
		return False

def split_pancakes(pancakes):
	#print pancakes
	split = [i for i in pancakes.split("+") if len(i) > 0]
	if pancakes[0] == "+":
			return 2*len(split)
			
	elif pancakes[0] == "-":
			return 2*len(split) -1


#f = open("A-large-practice.in",'r')
f = open("B-large.in",'r')
test_cases = int(f.readline())
out = open("results_B_large.txt",'w')
#print unique_digits_in_number(12333333345)

print test_cases
for i in range(test_cases):
    pancakes = f.readline().strip("\n")
    #print pancakes
    same_flip = are_pancakes_flipped_the_same(pancakes)
    #print same_flip
    if same_flip == '+':
        result = 0
    elif same_flip == '-':
        result = 1
    else:
        #result = "unknown yet"
        result = split_pancakes(pancakes)
    print result, pancakes
    output = output_format(result,i)
    out.write(output)

