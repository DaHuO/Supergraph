def solve():
    n=int(input())
    d={}
    for i in range(2*n-1):
        for j in input().split():
            if j not in d:
                d[j]=1
            else:
                d[j]+=1
    a=[]
    for i in d.keys():
        if d[i]%2:
            a+=[int(i)]
    a.sort()
    print(" ".join(map(str,a)))
        
if __name__ == "__main__":
    for i in range(int(input())):
        print("Case #%d: "%(i+1),end='')
        solve()