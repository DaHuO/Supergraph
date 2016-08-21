f = open("F:\InteresT\Python\ProblemSet4\Code Jam\cout.txt","w")
f.truncate()
p = open("F:\InteresT\Python\ProblemSet4\Code Jam\A-large.in","r+")
w = p.read()
w = w.split("\n")

T=w[0]
A=[0,1,2,3,4,5,6,7,8,9]
for i in range(int(T)):
    j=1
    N=w[i+1]
    if N=='0':
        y="Case #{}: {}".format(i+1,"INSOMNIA")
        f.write(str(y))
        f.write("\n")
    else:
        B=[]
        while True:
            k=j*int(N)
            for z in str(k):
                if int(z) in A:
                    if int(z) not in B:
                        B.append(int(z))
            B.sort()
            if A == B:
                y="Case #{}: {}".format(i+1,k)
                f.write(str(y))
                f.write("\n")
                break
            j=j+1
f.close()
p.close()