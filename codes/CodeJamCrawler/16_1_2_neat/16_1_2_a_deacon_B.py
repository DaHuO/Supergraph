



def solve(infile, outfile):
    cases = int(infile.readline())
    for i in range(cases):
        all_nums = {}
        result = []
        N = int(infile.readline())
        for j in range(N*2 - 1):
            nums = [int(i) for i in infile.readline().strip("\n").split()]
            for num in nums:
                if num in all_nums:
                    all_nums[num] += 1
                else:
                    all_nums[num] = 1
            #print(all_nums)
        for num in all_nums:
            if all_nums[num] % 2 == 1:
                result.append(num)
        result.sort()
        to_print = "Case #{}:".format(i+1)
        for thing in result:
            to_print += " " + str(thing)
        
        outfile.write(to_print+"\n")



if __name__ == '__main__':
    path = 'Data/'
    #name='B-sample'
    #name='B-small-attempt0'
    name='B-large'
    
    infile = open(path+name+'.in', 'r')
    outfile = open(path+name+'.out','w')
    
    solve(infile, outfile)
    infile.close()
    outfile.close()