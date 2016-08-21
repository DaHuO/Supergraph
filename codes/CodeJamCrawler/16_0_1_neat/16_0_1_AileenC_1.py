file = open("input")

counter_i = 1
counter_end_i = file.readline()
input_num = '0'
collected = []
result = 0
printxt=""

def solve(input_num, collected, result, printtxt):
	ini = int(input_num)
	while(collected!= [0,1,2,3,4,5,6,7,8,9] and result < 10001):
		result = result + 1
		input_num =str (result * ini)
		newcollected = map(int, input_num)
 	        collected= sorted(set(collected + newcollected))
		#print collected
	if (result < 10001):
		return str(input_num)
	else:
		return "INSOMNIA"

#def solve(a,num,helper):
#	helper = 0
#	it=1
#	sum=0
#	newhelp=0
#	while(it<num):
#		sum=a[it-1]+sum
#		if(a[it]>0 and it > sum):
#			newhelper = it-sum
#			sum = sum + newhelper
#			helper=helper+newhelper
#		it=it+1
#	return helper

while (counter_i <= int(counter_end_i.strip())):
	current_line = file.readline().strip()
	input_num = current_line
	#print input_num
	#solve(input_num, collected, result, printxt)
	print "%s%d%s%s"%("Case #",counter_i,": ",solve(input_num, collected, result, printxt))
	counter_i = counter_i + 1
