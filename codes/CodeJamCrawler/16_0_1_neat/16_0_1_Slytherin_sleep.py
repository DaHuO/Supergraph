tc = int(input())
for cs in range(1,tc+1):
    perfectSet = set('0123456789')
    emptySet = set()
    mySet =set()
    n = int(input())
    i = int(1)
    ans = "INSOMNIA"
    if(n!=0):
        while(True):
            number_string = str(n*i)
            for ch in number_string:
                mySet.add(ch)
            if(perfectSet-mySet == emptySet):
                break
            i=i+1
        ans = str(n*i)

    print ("Case #"+str(cs)+": "+ans)
