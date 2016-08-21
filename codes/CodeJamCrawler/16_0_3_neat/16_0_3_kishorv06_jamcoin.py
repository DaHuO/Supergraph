factors = {}
factor = ""

def isinvalid(val):
    global factor
    for k in range(3,12,2):
        if((val%(k))==0):
            factor += " " + str(k)
            return False
    return True

def isjamcoin(coin):
    global factor
    k = 2
    while(k<11):
        val = int(coin,k)
        if(isinvalid(val)):
            return False
        if(k != 10):
            factor += " 2"
        k += 2
    return True
        

def jamcoin(length,cases):
    global factor
    global factors
    coins = list()
    i = 0
    for j in range(cases):
        while(1):
            factor = ""
            coin = "{0:b}".format(i)+"1"
            coin = "1"+coin.zfill(length-1)
            if(isjamcoin(coin)):
                coins.append(coin)
                factors[coin] = factor
                i += 1
                break
            else:
                i += 1
        j += 1
    return coins

cnt = input()
m = 1
while(m <= cnt):
    v = raw_input()
    N = v.split()[0]
    J = v.split()[1]
    coins = jamcoin(int(N),int(J))
    print "Case #{0}:".format(m)
    for coin in coins:
        print coin+factors[coin]
    m += 1
    
        

