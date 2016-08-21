with open('input.txt') as f:
    tests = int(f.readline())
    for j in range(1, tests+1):
        str = f.readline()
        newstr=""
        
        newstr+=str[0]
        i = 1        
        while i < len(str):
            if str[i] >= newstr[0]:
                newstr=str[i]+newstr
            else:
                newstr+=str[i]
            i += 1
        
        print("Case #{}: {}".format(j,newstr))    