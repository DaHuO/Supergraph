import sys
sys.stdin = open("input.txt","r")
f = open("output.txt","w")


input()
n,j = map(int,input().split())

def is_prime(x) :
    if type(x)!= int :
        print("Type error in def is_prime")
        return 0

    if x%2==0 : return 2

    i = 3
    while i*i<=x :
        if x%i==0 : return i
        i+=2

    return 0

def get_ans(mask) :
    ans = [''.join([str(x) for x in mask[::-1]])]
    #print(mask)
    for base in range(2,11) :

        number = 0
        pw = 1
        
        for x in mask :
            number+=x*pw
            pw*=base

        #print("**",number)

        divisor = is_prime(number)
        if divisor == 0 :
            return 0
        ans.append(str(divisor))
    return ans

all_ans = []

def rec(mask) :
    if type(mask)!=list :
        print("Type error in def rec")
        return


    if len(all_ans)==j : return
    
    if len(mask)==n :
        x = get_ans(mask)
        if x!=0 :
            all_ans.append(' '.join(x))
        return

    if len(mask)==n-1 :
        mask.append(1)
        rec(mask)
    else :
        rec(mask+[0])
        rec(mask+[1])


rec([1])
f.write("Case #1:\n")
f.write('\n'.join(all_ans))


f.close()
