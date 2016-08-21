N_start = int("10000000000000000000000000000001",2)
ans = []
w = open("./2016_QR/C-small.ans",'w')
w.write('Case #1:\n')

for i in range(500):
    N_binary = bin(N_start + (i*2))
    N_binary = N_binary[2:]
    ans_list = []

    for j in range(2,11):
        cnum_find = False
        N = int(N_binary,j)
        for k in range(2,1000):
            if N % k == 0:
                ans_list.append(k)
                cnum_find = True
                break
        if cnum_find == False:
            break
    if len(ans_list) == 9:
        ans.append((N_binary))
        ans_list_str = map(str,ans_list)
        w.write(N_binary + " " + " ".join(ans_list_str)+ "\n")

    if len(ans) == 500:
        break
w.close()