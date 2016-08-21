#input_file = "input_test.in"
#input_file = "A-small-attempt0.in"
input_file = "A-large.in"
#output_file = "output_test.out"
#output_file = "output_small.out"
output_file = "output_large.out"



with open (input_file,'r') as input, open(output_file,'w') as output:
	num_cases = int(input.readline().strip())
	for j in range(num_cases):
		lista_boolean = [False]*10
		caso = int(input.readline())
		num_final = 0
		mult_N = 1
		if caso == 0:
			output.write("Case #{0}: INSOMNIA\n".format(j+1))
		else:
			while lista_boolean.count(True) != 10:
				caso_aux = caso * mult_N
				caso_split = [int(i) for i in str(caso_aux)]
				for i in caso_split:
					lista_boolean[i] = True
				mult_N += 1
			num_final = caso_aux
			output.write("Case #{0}: {1}\n".format(j+1,num_final))



