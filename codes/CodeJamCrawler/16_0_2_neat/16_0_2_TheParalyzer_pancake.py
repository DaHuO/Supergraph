
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

def solveAllSheep(filename,output_filename,num_threads):
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

def checkDone(pstack):
    return not bool(len(set(pstack)-set('+')))

def flipBits(pstack):
    return ''.join(['+' if pancake=='-' else '-' for pancake in pstack])

def switch(index,pstack):
    return flipBits(pstack[:index][::-1])+pstack[index:]

def findNeighbor(pstack):
    head = '+' if pstack[0]=='-' else '-'
    for i,p in enumerate(pstack):
        if p==head:
            return i
    return len(pstack)

def greedySort((pstack,problem_num)):
    count = 0
    while not checkDone(pstack):
        index = findNeighbor(pstack)
        #print index,pstack
        pstack = switch(index,pstack)
        count += 1
    return problem_num,str(count)

def solveAll(filename='pancake_test.txt',output_filename='pancake_test_output.txt',num_threads=50):
    input_data = open(filename).read().split('\n')
    print input_data
    number_of_problems = int(input_data[0])
    print number_of_problems
    input_data = input_data[1:-1]
    print input_data
    output_data = range(number_of_problems)
    pool = Pool(processes=num_threads)
    for i, status in enumerate(pool.imap_unordered(greedySort, zip(input_data,range(1,number_of_problems+1)))):
        print i,status
        output_data[status[0]-1] = 'Case #'+str(status[0])+': '+status[1]

    open(output_filename,'w').write('\n'.join(output_data))