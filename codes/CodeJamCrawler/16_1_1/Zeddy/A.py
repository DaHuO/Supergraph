import collections

if __name__ == "__main__":

    fin = open('A-large.in', 'r')
    fout = open('A-large.out', 'w')

    #fin = open('in.txt', 'r')
    #fout = open('out.txt', 'w')

    cases = int(fin.readline())
    print cases

    for t in range(0, cases):
        s = list(fin.readline().rstrip())
        r = collections.deque(s[0])
        if len(s) > 1:
            for i in range(1, len(s)):
                temp = r.popleft()
                r.appendleft(temp)
                if s[i] >= temp:
                    r.appendleft(s[i])
                else:
                    r.append(s[i])
        s = ''.join(r)

        print "Case #%d: %s" % (t+1, s)
        fout.write("Case #" + str(t+1) + ": " + s + "\n")

    fin.close()
    fout.close()