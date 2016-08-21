import sys
sys.stdin = open('B-large.in','r')
sys.stdout = open('B-large.out','w')
T = int(raw_input())
case = 0
while T:
    T -= 1
    count = 0
    string = raw_input()
    while True:
        out = string.rfind('-')
        if out == -1:
            break
        string = ''.join([(lambda s: '-' if s=='+' else '+')(i)for i in string[:(out+1)]])
        count += 1
    case += 1
    print "Case #%d: %d"%(case,count)
