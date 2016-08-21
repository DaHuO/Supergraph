import os, sys, time

def flip(s, end):
    if end == 0:
        s[0] = '+' if s[0] == '-' else '-'
        return s
    for i in xrange(0, end):
        s[i] = '+' if s[i] == '-' else '-'
    s[:end] = s[:end][::-1]
    return s

def pancake(s):
    # If single pancake
    if s[0] == '-' and len(s) == 1:
        return 1

    flag = '-' if s[0] == '+' else '+'
    count = 0
    while '-' in s:
        if s[0] == '-' and s[1:] == s[:-1]:
            count += 1
            return count

        for idx, k in enumerate(s):
            if k == '-' and flag == '-':
                s = flip(s, idx)
                flag = '+'
                count += 1
                break
            elif k == '+' and flag == '+':
                s = flip(s, idx)
                flag = '-'
                count += 1
                break
            else:
                continue
    return count

if __name__ == '__main__':
    out = open(sys.argv[2], 'w')
    f = open(sys.argv[1])
    testcases = f.readline()

    for i in xrange(1, int(testcases)+1):
        s = f.readline().strip()
        ans = pancake(list(s))
        res = "Case #{i}: {ans}\n".format(i=i, ans=ans)
        out.write(res)
