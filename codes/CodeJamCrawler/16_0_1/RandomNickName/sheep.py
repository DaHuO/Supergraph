def solve(start):
    if start == 0:
        return "INSOMNIA"
    remaining_digits = [x for x in range(0, 10)]
    counter = 1
    current = start
    tmp = 0
    while len(remaining_digits) > 0:
        tmp = [int(i) for i in list(str(current))]
        #print tmp
        for item in tmp:
            if item in remaining_digits:
                remaining_digits.remove(item)
        current = int(start) * counter
        counter = counter + 1
    return int(''.join(map(str, tmp)))
        

def main():
    exists = set()
    trueExists = exists
    create = set()
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    #l, d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print l,d,n
    for j in xrange(1, t+1):
        start = int(raw_input())
        #print start
        counter = 0
            
        answer = solve(start)  
        print "Case #{}: {}".format(j, answer) 


if __name__ == "__main__" :
    main()
    
