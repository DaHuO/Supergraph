from functools import lru_cache


@lru_cache(maxsize=None)
def solve(num):
    i = 1

    if i * num == (i + 1) * num:
        return "INSOMNIA"
    else:
        seen = [0 for i in range(10)]
        while not all(seen):
            t = i * num
            while t:
                seen[t % 10] = 1
                t //= 10
            i += 1
        return (i - 1) * num

T = int(input())

for u in range(T):
    N = int(input())

    print("Case #{}: {}".format(u + 1, solve(N)))
