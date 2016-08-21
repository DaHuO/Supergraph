def operate(s, i):
    ss = list(s)
    temp = ss[: i + 1]
    temp = [chr(ord('+') + ord('-') - ord(c)) for c in temp]
    temp.reverse()
    ss[: i + 1] = temp
    return ''.join(ss)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = (raw_input())  # read a list of integers, 2 in this case
    pos = s.rfind('-')
    step = 0
    while (pos != -1):
        if s.startswith('-'):
            s = operate(s, pos)
            pos = s.rfind('-')
            step += 1
        else:
            pos1 = s.rfind('+', 0, pos)
            s = operate(s,pos1)
            step += 1
    print 'Case #{}: {}'.format(i, step)



  # check out .format's specification for more formatting options