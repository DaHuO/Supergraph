from multiprocessing import Pool


# def findGridBad((slist,N,j)):

#     fgrid = np.zeros((N,N)) - 1

#     rows = [-1]*N
#     cols = [-1]*N

#     next_lowest = np.min(slist)
#     x,y = np.where(slist==next_lowest)

#     # choose either as the row or column
#     fgrid[0,:] = sgrid[y[0],:]

#     if len(x)>1:
#         fgrid[:,0] = sgrid[y[1],:]
#     sgrid = np.delete(sgrid,y[0],0)
#     if len(x)>1:
#         sgrid = np.delete(sgrid,y[1],0)
#     else:
#         #this is the missing one!

#     return i,str(slist[0])

def findGrid((slist,j)):
    values = list(set(slist))
    print values
    sgrid = np.array(slist)
    print sgrid
    row = []
    for v in values:
        if np.sum(sgrid==v)%2!=0:
            print v
            row.append(v)
    print row
    return j,' '.join([str(r) for r in sorted(row)])


def solveAll(filename='sgrid.test',output_filename='sgrid.test.out',num_threads=20):
    input_data = open(filename).read().split('\n')
    number_of_problems = int(input_data[0])
    input_data = input_data[1:-1]

    # split into problems
    slist = []
    count = 0
    for i in xrange(number_of_problems):
        N = int(input_data[count])
        count+=1
        sg = []
        for j in xrange(2*N-1):
            sg += [int(s) for s in input_data[count].split(' ')]
            count+=1
        print sg
        slist.append(sg[:])
    print slist

    output_data = range(number_of_problems)
    pool = Pool(processes=num_threads)
    for i, status in enumerate(pool.imap_unordered(findGrid, zip(slist,range(1,number_of_problems+1)))):
        print i,status
        output_data[status[0]-1] = 'Case #'+str(status[0])+': '+status[1]

    print output_data
    open(output_filename,'w').write('\n'.join(output_data))