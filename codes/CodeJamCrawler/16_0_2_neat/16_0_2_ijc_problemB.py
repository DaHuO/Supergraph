def flip(s):
    return ''.join('+' if c == '-' else '-' for c in s)

def f(s):
    n = 0
    while s:
        if s[-1] == '-':
            n += 1
            s = flip(s)
        s = s[:-1]
    return n

def main():
    T = int(input())
    for i in range(T):
        s = input()
        print("Case #{}: {}".format(i+1, f(s)))

if __name__ == '__main__':
    main()
