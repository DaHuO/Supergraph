case = int(input())
for a in range(case):
    n, j = list(map(int,input().strip().split())) # n = length; j = num jamcoins
    n -= 2
    print("Case #%i:" %(a + 1))
    index = 0
    while j > 0:
        inner = bin(index)[2:]
        string = '1' + '0' * (n - len(inner)) + inner + '1'
        divisors = ''
        status = True
        for k in range(2,11):
            for i in range(2,500):
                if int(string,k) % i == 0:
                    #print(int(string,k), i, int(string,k) % i)
                    divisors += ' ' + str(i)
                    break
                if i == 500:
                    status = False
            if status == False:
                break
        
        if len((string+divisors).split()) == 10:
            print(string + divisors)
            j -= 1
        index += 1
