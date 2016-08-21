import os

foldername = os.getcwd()
filename = "B-large"
f_i = open(os.path.join(foldername, filename+".in"))
T = int(f_i.readline())

if os.path.isfile(filename+".out"):
    os.remove(filename+".out")
f_o = open(filename+".out", 'w')

def serve(stack):
    for side in stack:
        if side == '-':
            return False
    return True

for case in range(T):
    S = f_i.readline().strip()

    ans = 0
    while not serve(S):
        top = S[0]
        i = 1
        while i != len(S) and S[i] == top:
            i += 1
        if top == '+':
            flip = '-'*i
        else:
            flip = '+'*i
        S = flip + S[i:]
        ans += 1
    
    f_o.write("Case #{}: {}\n".format(case+1,ans))

f_i.close()
f_o.close()