def solve(infile, outfile):
    cases = int(infile.readline())
    for i in range(cases):
        start = infile.readline().strip("\n")
        if start == '0':
            outfile.write("Case #{}: INSOMNIA\n".format(i+1))
        else:
            num = start
            N = 1
            tally = [0,0,0,0,0,0,0,0,0,0]
            is_done = False
            while not is_done:
                for char in num:
                    #print(char)

                    tally[int(char)] = 1
                if sum(tally) == 10:
                    outfile.write("Case #{}: {}\n".format(i+1, num))
                    is_done = True
                else:
                    N += 1
                    num = str(int(start) * N)
                    

if __name__ == '__main__':
    
    path = 'Data/'
    name = 'A-large'

    infile = open(path+name+'.in', 'r')
    outfile = open(path+name+'.out','w')
    
    solve(infile, outfile)
    infile.close()
    outfile.close()