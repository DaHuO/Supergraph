def Solution(label, line):
    cnt = 0
    l, r = 0, len(line)-1
    flag = True # T: find top
    while r>=0 and line[r] == '+':
        r-=1
    while l <= r:
        if flag:
            top = line[l]
            if top == '+':
                while l <= r and line[l] == top:
                    l+=1
                while l<=r and line[l]=='-':
                    l+=1
                cnt+=2
            elif top == '-':
                while l <= r and line[l] == top:
                    l+=1
                cnt+=1
            flag = False
        else:
            tail = line[r]
            if tail == '-':
                while l<=r and line[r] == tail:
                    r-=1
                while l<=r and line[r] == '+':
                    r-=1
                cnt+=2
            else:
                while l<=r and line[r] == tail:
                    r-=1
                cnt+=1
            flage = True

    print "Case #{}: {}".format(label, cnt)
    return 1



if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            out = Solution(i, line)
