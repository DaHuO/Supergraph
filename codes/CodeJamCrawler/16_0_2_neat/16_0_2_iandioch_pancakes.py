import sys

lines = sys.stdin.readlines()

n = int(lines[0])

for test in xrange(1, n+1):
    s = [c == '+' for c in lines[test][:-1]]
    while(len(s) > 0 and s[-1]):
        s = s[:-1]

    num_iter = 0
    while(len(s) > 0):
        count = 0 # num + at beginning
        for c in s:
            if c:
                count += 1
            else:
                break

        if count > 0:
            num_iter += 1
            t = []
            for i in xrange(count-1, -1, -1):
                t.append(not s[i])
            for i in xrange(count, len(s)):
                t.append(s[i])
            s = t
        
        s = [not c for c in s[::-1]]
        
        num_iter += 1
        while(len(s) > 0 and s[-1]):
            s = s[:len(s)-1]

    print 'Case #' + str(test) + ':', num_iter
    
