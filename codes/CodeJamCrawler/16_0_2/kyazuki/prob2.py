import re
T = input()
S = []
for i in xrange(T):
    S.append(raw_input())

def replace_pm(x):
    if x == '-':
        return '+'
    else:
        return '-'

case_num = 1
for i in S:
    stack = []
    cnt = 0
    for j in xrange(len(i)):
        stack.append(i[j])
    stack.reverse()
    #print stack
    while '-' in stack:
        for k in xrange(len(i)):
            if re.search('\-',''.join(stack)) != None:
                #print stack
                idx = re.search('\-',''.join(stack)).start()
                stack[idx:] = map(replace_pm, stack[idx:])
                cnt += 1
                #print stack
                break
    
    print "Case #{}: {}".format(case_num, cnt)
    case_num += 1
