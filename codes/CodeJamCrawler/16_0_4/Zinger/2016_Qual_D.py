import os

foldername = os.getcwd()
filename = "D-small-attempt0"
f_i = open(os.path.join(foldername, filename+".in"))
T = int(f_i.readline())

if os.path.isfile(filename+".out"):
    os.remove(filename+".out")
f_o = open(filename+".out", 'w')

for case in range(T):
    [K,C,S] = map(int,f_i.readline().split())

    ans = range(1,S+1)
    for _ in range(C-1):
        for i in range(S):
            ans[i] = K*(ans[i]-1)+i+1
    f_o.write("Case #{}: ".format(case+1))
    f_o.write(' '.join(map(str,ans)))
    f_o.write('\n')

f_i.close()
f_o.close()