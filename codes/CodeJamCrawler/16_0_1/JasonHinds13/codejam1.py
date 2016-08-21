f = open("A-large.in","r")
o = open("large-output.out","w")

seen = []
count = 1

ans = []

def change(x):
    x = str(x)

    for n in x:
        if n not in seen:
            seen.append(n)

T = int(f.readline())

for i in range(1, T+1):
    count = 1
    seen = []
    N = int(f.readline())

    if N == 0:
        ans.append("Case #"+str(i)+": INSOMNIA")

    else:
        
        while len(seen) != 10:
            change(N*count)
            count += 1

            if count >= (10**6):
                ans.append("Case #"+str(i)+": INSOMNIA")
                break
            
        if len(seen) == 10:
            ans.append("Case #"+str(i)+": "+str((count-1)*N))

for a in ans:
    o.write(a+"\n")
    print a

f.close()
o.close()
