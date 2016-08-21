__author__ = 'ben'
jamCoinCount = 0

trivialDiv = [2, 3, 5, 7, 11, 13]

o = open("out", "w")

def notPrimeCheck(n):
    for t in trivialDiv:
        if n%t == 0:
            return t
    return False

def validateJamCoin(jc):
    jamCoinVal = []
    for b in range(2, 11):
        nptest = notPrimeCheck(int(jc, b))
        if not nptest:
            return False
        else:
            jamCoinVal.append(nptest)
    return jamCoinVal

c = 0
o.write("Case #1:\n")
while jamCoinCount < 500:
    jamCoin = '1'+'{0:030b}'.format(c) + '1'
    vj = validateJamCoin(jamCoin)
    if vj:
        ver = ""
        for v in vj:
            ver += " " + str(v)
        o.write(jamCoin + ver + "\n")
        jamCoinCount += 1
    c += 1