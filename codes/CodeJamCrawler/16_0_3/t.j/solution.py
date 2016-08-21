from math import sqrt
from itertools import count, islice

input_file = open('C-small-attempt0.in', 'r')
input_file.readline()
base_list = (2,3,4,5,6,7,8,9,10)

input_array =input_file.readline().split()
N = int(input_array[0])
J = int(input_array[1])
input_file.close()
print N,J

counter = 0
current_jamcoin = '1' + '0'*(N-2) + '1'
# current_jamcoin = '100011'
final_array = []

while counter < J:
	print current_jamcoin
	answer = [current_jamcoin]
	failure = False
	
	for i in base_list:
		num = int(current_jamcoin, i)

		for j in islice(count(2), int(sqrt(num)-1)):
			failure = True
			if not num%j:
				answer.append(j)
				failure = False
				break


		if failure == True:
			break
		
	if failure == False:
		output_line = ' '.join(map(str, answer))
		final_array.append(output_line)
		print "Jamcoin Found"
		counter += 1

	current_jamcoin = bin(int(current_jamcoin, 2) + 2)[2:N+2]
	
	
output_file = open('output.txt', 'w')
output_file.write('Case #1:\n')
for i in range(0,len(final_array)):
        output_file.write(final_array[i])
        if i != (J-1):
                output_file.write('\n')
output_file.close()

print "Done"
