

def solve(n):
    ans = set()
    for i in range(1, 1000000):
        ans.update(set(str(n * i)))
        if len(ans) == 10:
            return str(n * i)
    return "INSOMNIA"


def main():
    t = int(input())
    ans_list = []
    for i in range(t):
        n = int(input())
        ans_list.append(solve(n))

    for i, ans in enumerate(ans_list, start=1):
        print("Case #{0}: {1}".format(i,  ans))

if __name__ == '__main__':
    main()
