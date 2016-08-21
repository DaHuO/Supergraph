import sys
sys.stdin=open("d-small.in",'r')
sys.stdout=open("d-small.out",'w')
for t in xrange(1,int(raw_input())+1):
    K,C,S=map(int,raw_input().split())
    print 'Case #%i:'%(t),
    curr=1
    while curr<K**C+1:
        print curr,
        curr+=K**(C-1)
    print
sys.stdout.close()
