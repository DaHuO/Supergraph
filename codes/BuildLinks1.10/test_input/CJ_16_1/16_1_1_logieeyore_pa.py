import sys

def print_result(line_cnt, result):
    print "Case #%s: %s" % (line_cnt, result)

def last_word(s,r,line_cnt):
    for h in range(0,len(s)):
        current = s.pop(0)
        first=r[0]
        last=r[-1]
        if current >= first:
            r.insert(0,current)
        else:
            r.append(current)
        #last_word(s,r,line_cnt)
    print_result(line_cnt,"".join(r))
    return


def solve_template():
    T = int(sys.stdin.readline().rstrip())
    line_cnt=1
    while 1:
        l = list(sys.stdin.readline().rstrip())
        r = list()
        r.append(l.pop(0))
        last_word(l,r,line_cnt)
        
        if line_cnt == T:
            break
        line_cnt+=1

if __name__=="__main__":
    solve_template()
