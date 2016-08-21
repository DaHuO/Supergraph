from collections import deque

test_cases = int(raw_input())


def solve(S):
    tmp = deque()
    str_list = [ch for ch in S]
    i = 1
    for indx in xrange(len(str_list)):
        if indx == 0:
            tmp.extendleft(S[indx])
            continue
        if ord(str_list[indx]) >= ord(tmp[0]):
            tmp.extendleft(S[indx])
            i += 1
        else:
            tmp.extend(S[indx])

    return ''.join(tmp)


for t in xrange(test_cases):
    string = str(raw_input())
    print "Case #%d: %s" % (t + 1, solve(string))
