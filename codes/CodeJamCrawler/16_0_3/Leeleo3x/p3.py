from multiprocessing import Pool, Process, Value, Manager
import threading

memo = {}

def getBegin(x, length):
    return x ** 0 + (x ** (length - 1))

def isPrime(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        return 2
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            memo[n] = i
            return i
    memo[n] = -1
    return -1

length = int(input())


# for i in range(2, 11):
#     num.append(getBegin(i, length))

count = int(input())

start = getBegin(2, length)
manager = Manager()
num = manager.list()

def calculate(current, num):
    for i in range(2, 11):
        cur = int(bin(current)[2:], i)
        if isPrime(cur) == -1:
            return
    num.append(current)

def getList(current):
    res = []
    for i in range(2, 11):
        cur = int(bin(current)[2:], i)
        res.append(str(isPrime(cur)))
    return res

pool = []

def max_excute(p):
    p.join(5)
    if p.is_alive():
        print("terminate")
    p.terminate()


for _ in range(4):
    pool.append(Process())
current = start
while len(num) < count:
    print(len(num))
    for p in pool:
        if not p.is_alive():
            p = Process(target=calculate, args=(current, num, ))
            p.start()
            threading.Thread(target=max_excute, args=(p, )).start()
            current += 2

for p in pool:
    if p.is_alive():
        p.terminate()

f = open("data.out", "w+")
f.write("Case #1:\n")
# print(len(num))
for idx in range(count):
    print(bin(num[idx])[2:])
    f.write(bin(num[idx])[2:] + " " + " ".join(getList(num[idx])) + "\n")
