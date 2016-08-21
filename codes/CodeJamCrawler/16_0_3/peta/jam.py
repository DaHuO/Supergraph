def factor(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return i
    return None

n = 16
count = 0
jamnumber = int('1' + 14*'0' + '1', 2)
print("Case #1:")
while count < 50:
    prime = False
    factors = []
    for i in range(2, 11):
        number = int(bin(jamnumber)[2:], i)
        factors.append(factor(number))
        if factors[-1] == None:
            prime = True
            break
    if not prime:
        print(bin(jamnumber)[2:], " ".join([str(x) for x in factors]))
        count += 1
    jamnumber += 2


