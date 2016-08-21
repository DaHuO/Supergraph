import random;

def gen (N):
    arr = [0]*10
    i = 1
    while True:
        n = N*i
        i += 1
        k = [int(j) for j in str(n)];
        for e in k:
            arr[e] = 1;
        
        if arr == [1] * 10:
            return n
        
        
 
if __name__ == '__main__':
    t = map(int, raw_input().split())[0];
    
    for i in range (t):
        n = map(int, raw_input().split())[0];
        if n == 0:
            print "Case #%d: INSOMNIA" % (i+1)
            continue;
        print "Case #%d:"  % (i+1), gen (n)
