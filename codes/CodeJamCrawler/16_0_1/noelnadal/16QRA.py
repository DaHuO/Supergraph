"""B = ["INSOMNIA"]
C = "0123456789"
for N in range(1,1+10**6):
    if N % 1000 == 0:
        print(N)
    n = N
    A = [0 for _ in range(10)]
    while sum(A) < 10:
        s = str(n)
        for i in range(len(s)):
            A[C.index(s[i])] = 1
        n = n + N
    B += [n-N]
f = open("tableau.txt","w")
f.write(str(B))
f.close()
"""
R = []
C = "0123456789"
f = open("input.txt","r")
T = int(f.readline())
for k in range(T):
    N = int(f.readline().strip())
    n = N
    A = [0 for _ in range(10)]
    while sum(A) < 10 and n > 0:
        s = str(n)
        for i in range(len(s)):
            A[C.index(s[i])] = 1
        n = n + N
    if n == 0:
        R += ["INSOMNIA"]
    else:
        R += [n-N]
f.close()
f = open("output.txt","w")
for k in range(T):
    f.write("Case #"+str(k+1)+": "+str(R[k])+"\n")
f.close()
