import sys

def print_result(line_cnt, result):
    print "Case #%s: %s" % (line_cnt, result)

def counting_sheep(n,rn,i,chk,line_cnt):
    if n == 0: 
        print_result(line_cnt,"INSOMNIA")
        return
    arr = list(str(n))
    for a in arr:
        chk[int(a)] = 1
#    print >> sys.stderr, n,i,chk
    if len(chk.keys()) == 10:
        print_result(line_cnt,n)
        return
    else:
        counting_sheep(n+rn,rn,i+1,chk,line_cnt)
    

def solve_template():
    T = int(sys.stdin.readline().rstrip())
    line_cnt=1
    while 1:
        l = sys.stdin.readline().rstrip()
        chk=dict()
        i = 1
        
        counting_sheep(int(l),int(l),i,chk,line_cnt)
        
        if line_cnt == T:
            break
        line_cnt+=1

if __name__=="__main__":
    solve_template()
