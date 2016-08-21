import sys


def counting_sheep(n):
    numbers = set(['0','1','2','3','4','5','6','7','8','9'])
    count = 0
    while numbers and n != 0:
        count = count + 1
        last = count * n
        numbers = numbers - set(str(last))
    return last if n != 0 else 'INSOMNIA'

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        result = counting_sheep(int(sys.stdin.readline()))
        print("Case #{}: {}".format(t, result))

if __name__ == "__main__":
    # execute only if run as a script
    main()
