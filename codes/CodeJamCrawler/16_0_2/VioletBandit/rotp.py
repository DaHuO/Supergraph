f = open('input.txt', 'r')
fout = open('output.txt', 'w+')
#str = raw_input("enter: ");
#str = '+-+-+-----+'
total = int(f.readline())
print total
for i in range(total):
    str = f.readline();
    n = m = 0
    last = 'a'
    for c in str:
        if c == '-' and last == 'a':
            n = 1
        elif c == '-' and last == '+':
            m += 1
        elif c == '-' and last == '-':
            pass
        elif c == '+':
            pass
        last = c
    print "Case #%d: %s %d" % (i+1, str[:-1], n + 2 * m)
    fout.write("Case #%d: %d\n" % (i+1, n + 2 * m))
f.close()
fout.close()
print len("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
