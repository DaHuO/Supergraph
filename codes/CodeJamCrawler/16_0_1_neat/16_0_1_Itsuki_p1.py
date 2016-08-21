import sys

def solve(N):
    count = [0] * 10
    mul = 0

    if N == 0:
        return -1

    while 0 in count:
        mul = mul + 1
        digit = list(map(int, str(mul * N)))
        for i in range(0, len(digit)):
            count[digit[i]] = 1
    return mul*N

def main():
    result = []
    T = sys.stdin.readline().strip()
    for i in range(0, int(T)):
        N = sys.stdin.readline().strip().split()
        result.append(solve(int(N[0])))

    for i in range(0, len(result)):
        if result[i] == -1:
            print("Case #%d:" % (i+1)), 'INSOMNIA'
        else:
            print("Case #%d:" % (i+1)), result[i]

if __name__=="__main__":
    main()
