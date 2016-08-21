################## Elena Khusainova #####################

################## Functions ############################
def next_coin(jamcoin, N):
    i = 1
    answer = []
    while jamcoin[-i] == 1 and i < N:
        i += 1

    if i < N:
        for j in range(N-i):
            answer += [jamcoin[j]]
        for j in range(N-i,N-1):
            answer += [1-jamcoin[j]]
        answer += [1]
            
    return(answer)

def firstdivisor(n, m):
    t = int(n ** 0.5) + 1
    for i in range(2, min(t,m)):
        if n % i == 0:
            return i
    return 0

######################### Main ##########################
N = 32
J = 500

with open("Problem4Large_out.txt", "a") as myfile:
    myfile.write('Case #1:' + '\n')
myfile.close()

curr=[0] * N
curr[0], curr[-1] = 1,1

it = 1    
while it <= J:
    divisors = []
    check = True
    for base in range(2,11):
        temp = 0
        for j in range(1,N+1):
            if curr[-j]:
                temp += base ** (j-1)
        fd = firstdivisor(temp, 12)
        if not fd:
            check = False
            break
        else:
            divisors += [fd] 
    if check:
        str1 = [str(s) for s in curr]
        str2 = [str(s) for s in divisors]
        
        with open("Problem4Large_out.txt", "a") as myfile:
            myfile.write(''.join(str1)+' '+' '.join(str2)+'\n')
        myfile.close()
        it += 1

    curr = next_coin(curr, N)
        

