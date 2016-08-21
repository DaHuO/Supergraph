#counting sheep

from sys import stdin, stdout

inp_file = open("A-large.in","r")
out_file = open("A.out","w")

def process(num):
	
	flag = [0 for i in range(10)]
	current_num = num

	while True:
		
		for x in str(num):
			flag[int(x)] = 1

		stop = True
		for i in range(10):
			if flag[i] == 0:
				stop = False

		if stop == True:
			return num

		num += current_num

num_array = inp_file.read().split('\n')

for i in range(1, int(num_array[0])+1):
	if int(num_array[i]) == 0:
		res = 'INSOMNIA'
	else:
		res = str(process(int(num_array[i])))
	#print(res)
	out_file.write("Case #" + str(i) + ": "+ res + "\n")


inp_file.close()
out_file.close()
