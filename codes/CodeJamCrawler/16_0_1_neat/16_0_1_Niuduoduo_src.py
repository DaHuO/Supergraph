#! /usr/bin/env python
def get_stream(file):
	for line in file:
		for token in line.strip().split():
			yield token
 
def get_int(stream):
	retour = int(stream.next())
	return retour
 
def get_solution(stream):

#mise ne forme
#=============

	#nombre de parfums
	N = get_int(stream)
 	#print "N = " + str(N)
	
	#tableau bool 0 a 9
	num_bool = [0]*10
	
	
#traitement
#==========

	if N == 0: return "INSOMNIA"
	else:
		sum_cum = 0
		all_num_find = False
		#return 10
		while 1:#sum_cum<150:
			sum_cum += N
			#print list(str(sum_cum))
			for num in list(str(sum_cum)):
				if num == "0": num_bool[int(num)] = 1
				if num == "1": num_bool[int(num)] = 1
				if num == "2": num_bool[int(num)] = 1
				if num == "3": num_bool[int(num)] = 1
				if num == "4": num_bool[int(num)] = 1
				if num == "5": num_bool[int(num)] = 1
				if num == "6": num_bool[int(num)] = 1
				if num == "7": num_bool[int(num)] = 1
				if num == "8": num_bool[int(num)] = 1
				if num == "9": num_bool[int(num)] = 1
			if sum(num_bool)==10:
				#print num_bool
				#print sum(num_bool)
				return sum_cum
				
	#Boucle

	

def main(path): 
	#print "Fonction main\n"
	file = open(path, 'r')
	outfile = open(path + '.out', 'w')
	stream = get_stream(file)  
	cases = get_int(stream)
	  
	solution = []
	for case in range(0, cases):
		solution = get_solution(stream)
		buffer = "Case #" + str(case+1) + ": " + str(solution) + "\n"
		outfile.write( buffer )
		#print buffer
 
	outfile.close()

print "Appel traitement\n"
main("in")



