import os

foldername = os.getcwd()
filename = "A-large"
f_i = open(os.path.join(foldername, filename+".in"))
T = int(f_i.readline())

if os.path.isfile(filename+".out"):
    os.remove(filename+".out")
f_o = open(filename+".out", 'w')

for case in range(T):
    N = int(f_i.readline())

    if N is 0:
        f_o.write("Case #{}: INSOMNIA\n".format(case+1))
        continue
    
    awake = True
    seen = [0]*10
    i = 0
    while awake:
        i += 1
        num = i*N
        for dig in str(num):
            seen[int(dig)] = 1
        if seen == [1]*10:
            awake = False

    f_o.write("Case #{}: {}\n".format(case+1,num))

f_i.close()
f_o.close()