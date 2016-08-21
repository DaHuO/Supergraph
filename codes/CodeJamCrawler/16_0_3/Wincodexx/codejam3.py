
def jam(i):
    if i[0] != "1" or i[len(i)-1] != "1":
        return False
    answer = i
    for j in xrange(2,11):
        num = toBase(i,j)
        this = prime(num)
        if this == None:
            return False
        answer += (" "+ str(this))
    print answer
    return True

def getAll(N,J):
    res = []
    count = 0
    while len(res) != J:
        re = '{0:016b}'.format(count)
        if jam(re):
            res.append(re)
        count+=1

def toBase(res,base):
    total = 0
    res = res[::-1]
    for i in xrange(len(res)) :
        total += int(res[i]) * (base**i)

    return total

def prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return None



if __name__ == "__main__":
    leggo = dict()
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    x = f.readline()
    idk = x.split(" ")
    N = idk[0]
    J = idk[1]
    print("Case #1:")
    getAll(int(N),int(J))

