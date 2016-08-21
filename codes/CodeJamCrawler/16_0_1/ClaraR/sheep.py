def Solution():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        N = int(raw_input()) #[int(s) for s in raw_input()]  # read a list of integers, 2 in this case
        
        if N == 0:
            print "Case #{}: INSOMNIA".format(i)
            continue
    
        j = 1
        seen = [k for k in range(10)]
        while True:
            
            num = j * N
            
            for digit in str(num):
                seen[int(digit)] = -1
            
            if sum(seen) == -10:
                print "Case #{}: {}".format(i, num)
                break
        
            j += 1
    
if __name__ == "__main__":
    Solution()