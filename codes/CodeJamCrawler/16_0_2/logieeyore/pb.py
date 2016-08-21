import sys

def print_result(line_cnt, result):
    print "Case #%s: %s" % (line_cnt, result)


def surpress(l): 
    # merge nearby character
    arr = list(l)
    t = []
    t.append(arr.pop(0))
    for i in range(0,len(arr)):
        lastone = t[-1]
        currentone = arr[i]
        if lastone == currentone:
            continue
        else:
            t.append(currentone)
    return t

def pancake(l,line_cnt):
    # surpress l to t
    # - merge nearby character
    t = surpress(l)
    # - trash tail plus character
    if t[-1] == "+":
        t.pop()
    # - trash tail plus character
    # len(t) is result 
    print_result(line_cnt, len(t))

def solve_template():
    T = int(sys.stdin.readline().rstrip())
    line_cnt=1
    while 1:
        l = sys.stdin.readline().rstrip()
        
        pancake(l,line_cnt)
        
        if line_cnt == T:
            break
        line_cnt+=1

if __name__=="__main__":
    solve_template()
