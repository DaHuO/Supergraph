def cnt(n):
    res = [False]*10
    i, num = 1, n
    while n and not all(res):
        extract(num, res)
        i += 1
        num = i * n
    return num - n if (num - n) else 'INSOMNIA'

def extract(n, res):
    while n > 0:
        res[n%10] = True
        n //= 10

def cnt_m():
    T = int(input())
    for i in range(T):
        print("Case #" + str(i+1) + ":", cnt(int(input())))

if __name__ == '__main__':
    cnt_m()