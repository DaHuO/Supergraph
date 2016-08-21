T = input()

for t in range(T):
    K, C, S = raw_input().split()
    K, C, S = [int(i) for i in K, C, S]
    
    print "Case #{0}:".format(t+1), ' '.join([str(i+1) for i in range(S)])
