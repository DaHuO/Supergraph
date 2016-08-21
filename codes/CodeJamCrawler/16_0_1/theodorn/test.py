from sys import stdout

def init_seen():
	return [0] * 10
	
def check_seen(num,seen):
	mystr = str(num);
	for char in (mystr):
		dindex = ord(char)-48;
		seen[dindex] = 1;
	for i in ( range(10) ):
		if( seen[i] == 0 ): return False
	return True

def check_number(num):
	if( num == 0 ): return "INSOMNIA"
	seen = init_seen()
	current_num = 0;
	i = 0;
	while( i <= 200 ):
		i += 1
		current_num += num
		if( check_seen(current_num,seen) ):
			break

	if(False):
		if( i > 72 ): 
			print str(num).rjust(6) + " | iter:" + str(i) + ", magic:" + str(current_num)
		if( (num % 10000) == 0 ): stdout.write(".")
	return str(current_num)

def read_input():
	arr = [];
	f = open( "input.txt" )
	num = int(f.readline().rstrip( "\n" ).rstrip( "\r" ))
	for line in f:
		line = line.rstrip( "\n" ).rstrip("\r");
		arr.append(int(line))
	if( num != len(arr) ):
		print "ERROR IN INPUT! " + str(num) + "," + str(len(arr))
		return []
	return arr

input_arr = read_input()
n_cases = len(input_arr)
for i in range(n_cases):
	result = check_number(input_arr[i])
	print "Case #" + str(i+1) + ": " + result

