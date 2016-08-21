def solve(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        flag = range(10)
        # print flag
        i = 0
        n_str = ''
        while (len(flag) > 0):
            i = i + 1
            n_str = str(n*i)
            # print n_str
            for digit_str in n_str:
                digit = int(digit_str)
                if digit in flag:
                    flag.remove(digit)
            # print flag
        return n_str

f_read = open('A-large.in','r')
f_write = open('A-large.out','w')
t = int(f_read.readline())
for k in range(t):
    n = int(f_read.readline())
    f_write.write('Case #{0}: {1}\n'.format(str(k+1),solve(n)))
f_read.close()
f_write.close()
