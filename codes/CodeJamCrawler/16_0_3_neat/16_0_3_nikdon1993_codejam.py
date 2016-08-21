import sys
sys.stdout = open('output.txt', 'w')

p = [0]*1000006
primes = []
for i in range(2, 1000006):
    if p[i]==0:
        primes.append(i)
        j = 2
        while j*i<1000006:
            p[i*j]=1
            j+=1


def generate_sol(jamcoin):
    ans = []
    for base in range(2, 11):
        is_valid_jamcoin = 0
        for prime in primes :
            if prime >= jamcoin :
                break
            value_in_base = 0
            pow_of_b = 1
            tmp = jamcoin
            while tmp > 0:
                if tmp%2==1:
                    value_in_base += pow_of_b
                pow_of_b *= base
                tmp /= 2
            if value_in_base%prime == 0:
                is_valid_jamcoin = 1
                ans.append(prime)
                break
        if is_valid_jamcoin==0:
            return []
    return ans

def cross_check(jamcoin, ans):
    for base in range(2, 11):
        value = 0
        pow_of_base = 1
        tmp = jamcoin
        while tmp:
            if tmp%2==1:
                value += pow_of_base
            pow_of_base*=base
            tmp/=2
        if value == ans[base-2]:
            return 0
        if value%ans[base-2] != 0:
            return 0
    return 1


t = input()

for tc in range(t):
    print "Case #"+str(tc+1)+":"
    n,j = map(int, raw_input().split())
    t = 1
    i = 0
    while i < (2**(n-1)):
        jamcoin = (2**(n-1)) + i*2 + 1
        ans = generate_sol(jamcoin)
        if len(ans)==0:
            i+=1
            continue
        s = ""
        while jamcoin:
            s = str(jamcoin%2)+s
            jamcoin/=2

        """"""
        print s,
        for e in ans[:-1]:
            print e,
        print ans[-1]
        
        """
        print s
        for b in range(2, 11):
            val = int(s, b)
            if val%ans[b-2]!=0:
                print "Got it wrong!!!!!!!!!!"
                exit()
            print "base:", b,"val:",val, "divisor:", ans[b-2], "mod:", val%ans[b-2] 
        if(cross_check(jamcoin, ans) == 0):
            print "Wrong"
        """
        
        j-=1
        if(j==0):
            break
        i+=1
