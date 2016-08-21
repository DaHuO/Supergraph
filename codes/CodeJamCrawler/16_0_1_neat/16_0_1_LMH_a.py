input = open('./al.in')
output = open('./al.out', 'w')

T = int(input.readline())
for k in range(1, T + 1):
    N = int(input.readline())
    ans = 'INSOMNIA'
    if(N != 0):
        f = [0] * 10
        done = True
        for i in range(1, 101):
            done = True
            num = N * i
            rec = i
            for x in str(num):
                f[int(x)] += 1
            for x in f:
                if(x == 0):
                    done = False
            if(done):
                ans = num
                break
    output.write('Case #%d: %s\n' % (k, ans))