f = open('C:\\study\\gjam\\jam2016\\A-large.in')
f_out = open('C:\\study\\gjam\\jam2016\\A-large_res.txt','w+')

T = int(f.readline())

for i in range(T):
    n = int(f.readline())
    digits = [0 for ii in range(10)]
    cnt = 1
    while True:
        n_str = str(n*cnt)
        for k in range(len(n_str)):
            digits[int(n_str[k])] = 1
        if (sum(digits) == 10 or n == 0):
            break
        cnt = cnt + 1
        
    res = str(cnt*n)
    if (n == 0):
        res = "INSOMNIA"
    f_out.write("Case #"+str(i+1)+": "+res+'\n')

f.close()
f_out.close()