def f(x):
    if x == 0:
        return None
    seen = set()
    n = 0
    while seen != set(map(str, range(10))):
        n += x
        seen |= set(str(n))
    return n

def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        print("Case #{}: {}".format(i+1, f(n) or 'INSOMNIA'))

if __name__ == '__main__':
    main()
