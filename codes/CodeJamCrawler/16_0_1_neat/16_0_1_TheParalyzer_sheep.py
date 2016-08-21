
def checkNumber(n,max_tries=5000,debug=False):
	remain = set(['0', '1', '2', '3', '4', '5', '6', '7', '8','9'])

	n_now = 0
	for N in range(max_tries):
		n_now = n + n_now
		n_now_set = set(str(n_now))
		remain = remain - n_now_set
		if debug:
			print remain
		if len(remain)==0:
			print n_now,N+1
			break


def checkNum(n,max_tries=100000000):
	remain = set(['0', '1', '2', '3', '4', '5', '6', '7', '8','9'])
	n_now = 0
	for N in range(max_tries):
		n_now = n + n_now
		n_now_set = set(str(n_now))
		remain = remain - n_now_set
		if len(remain)==0:
			return str(n_now)
	return 'INSOMNIA'

def checkNum2((n,index)):
	remain = set(['0', '1', '2', '3', '4', '5', '6', '7', '8','9'])
	n_now = 0
	for N in range(100000000):
		n_now = n + n_now
		n_now_set = set(str(n_now))
		remain = remain - n_now_set
		if len(remain)==0:
			return index,str(n_now)
	return index,'INSOMNIA'

from multiprocessing import Pool

def solveAll(filename,output_filename,num_threads):
    input_data = open(filename).read().split('\n')
    print input_data
    number_of_problems = int(input_data[0])
    print number_of_problems
    output_data = range(number_of_problems)
    input_data = [int(n) for n in input_data[1:-1]]
    print input_data

    pool = Pool(processes=num_threads)
    for i, status in enumerate(pool.imap_unordered(checkNum2, zip(input_data,range(1,number_of_problems+1)))):
    	print i,status
    	output_data[status[0]-1] = 'Case #'+str(status[0])+': '+status[1]

    open(output_filename,'w').write('\n'.join(output_data))