tests=int(input())
for test in range(1,tests+1):
    ans=set()
    n=int(input())
    for i in range(n*2-1):
        ls=list(map(int,input().split()))
        for ele in ls:
            if ele in ans:
                ans.remove(ele)
            else:
                ans.add(ele)

    print ("Case #{}: {}".format(test,' '.join(map(str,sorted(list(ans))))))
