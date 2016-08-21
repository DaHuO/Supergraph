def solve(k,c,s) :
    ret = -1
    
    return ret
def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    #l, d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print l,d,n
    global all_primes

    for j in xrange(1, t+1):
        k,c,s = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in
        #k tiles, 
        #c complexity (number of levels = c + 1)
        #s grad students
        #print k,c,s
        answer = "HUH?"
        answer = ""
        if k > s :
            answer = "IMPOSSIBLE"
        else :
            while s != 0:
                answer = answer + " " + str(s)
                s = s - 1
        print "Case #{}: ".format(j) + str(answer)
        
        
if __name__ == "__main__" :
    main()
