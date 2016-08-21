x = int(input())
for i in range(0, x):
    tope = '+'
    hil = input() + '+'
    hilera = list(hil)
    n = 0
    aux = hilera[0]
    for j in range(0, len(hilera)):
        if j != 0 and hilera[j - 1] != hilera[j]:
            mmm = hilera[j]
            n = n + 1
            for k in range(0, j ):
                hilera[k] = mmm
                aux = hilera[0]
    print('Case #' + str(i + 1)+':', n)