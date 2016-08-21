import sys
sys.stdin = open('A-large.in','r')
sys.stdout = open('A-large.out','w')
T = int(raw_input())
count = 1
while T:
    i = 1 
    N = raw_input()
    temp, Y = set(N), N
    if Y == "0":
        print "Case #%d: INSOMNIA"%count
    else:
        while True:
            temp.update(Y)
            if len(temp) == 10:
                print "Case #%d: %d"%(count,int(Y))
                break
            i += 1
            Y = str(i*int(N))
    T -= 1
    count += 1

