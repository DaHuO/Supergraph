
finam = 'in11.txt'
fonam = 'out11.txt'
fi = open(finam)
fo = open(fonam, 'w')
T = int(fi.readline())
for t in range(T):
    N = int(fi.readline())
    res = set()
    for m in range(1,100):
        num0 = N * m
        num = num0
        while num != 0:
            res.add(num % 10)
            num /= 10
        if len(res) >= 10:
            break
    sol = 'Case #'+str(t+1)+': '
    if len(res) < 10:
        sol += 'INSOMNIA'
    else:
        sol += str(num0)
    print sol
    fo.write(sol+'\n')
fo.close()

        
