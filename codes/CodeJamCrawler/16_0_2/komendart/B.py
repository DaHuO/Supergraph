def solve(s):
    a = [0 if i == '-' else 1 for i in s]
    ans = 0
    inv = 0
    for i in reversed(a):
        if (i ^ inv) == 0:
            inv ^= 1
            ans += 1
    return ans

def main():
    with open("input.txt") as fin, open("output.txt", 'w') as fout:
        T = int(fin.readline())
        for i in range(1, T + 1):
            print("Case #{0}: ".format(i), end='', file=fout)
            s = fin.readline().strip()
            print(solve(s), file=fout)
    
    
main()