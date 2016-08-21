def maxIndex(arr,to):
    i = 0
    maxIn = 0
    maxNum = 0
    ct = 0
    while i<to:
        if arr[i]=='+':
            ct+=1
        else:
            ct-=1
        if ct>maxNum:
            maxNum = ct
            maxIn = i
        i+=1
    return maxIn

def opp(sym):
    if sym=='+':
        return '-'
    else:
        return '+'

def flip(arr,froma,to):
    while True:
        if froma>to:
            return
        else:
            afroma = arr[froma]
            ato = arr[to]
            arr[froma] = opp(ato)
            arr[to] = opp(afroma)
            froma+=1
            to-=1
            
test = int(input())
for it in range(test):
    string = list(input())
    last = len(string) - 1
    ans = 0
    while '-' in string:
        while string[last]=='+': last-=1
        if string[last]=='-' and string[0]=='+':
            maxIn = maxIndex(string,last)
            flip(string,0,maxIn)
            ans+=1
        flip(string,0,last)
        ans+=1
    print("Case #{}: {}".format(it+1,ans))
