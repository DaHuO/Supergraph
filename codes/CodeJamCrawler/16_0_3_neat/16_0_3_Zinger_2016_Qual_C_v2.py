import os

foldername = os.getcwd()
filename = "C-large"

f_i = open(os.path.join(foldername, filename+".in"))
T = int(f_i.readline())
[N,J] = map(int,f_i.readline().split())
f_i.close()

if os.path.isfile(filename+".out"):
    os.remove(filename+".out")
f_o = open(filename+".out", 'w')

f_o.write("Case #{}:\n".format(T))

def proof(n):
    i = 2
    while i <= 7:
        if n % i == 0:
            return i
        i += 1
    return 0

coin = 2**(N-1)+1
while coin < 2**N:
    
    isjam = True
    ans = [0]*10
    for base in range(2,11):
        num = int(str(bin(coin))[2:],base)
        p = proof(num)
        if p == 0:
            isjam = False
            break
        ans[base-1] = p
    ans[0] = num

    if isjam:
        f_o.write(' '.join(map(str,ans)))
        f_o.write('\n')
        J -= 1
        if J == 0:
            break

    coin += 2

f_o.close()