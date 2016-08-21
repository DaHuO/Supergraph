#/usr/bin/env python3
def digits_in_dec(N):
    return set(str(N))

def solve_for_N(N, s, i):
    if len(s) == 10:
        return (i-1) * N
    if i > 100:
        return None

    return solve_for_N(N, s.union(digits_in_dec(i*N)), i+1)

def solve_case(case):
    N = int(input())

    result = solve_for_N(N, set(), 1) 

    if result is None:
        result = "INSOMNIA"

    print("Case #{0}: {1}".format(case, result))


def main():
    cases = int(input())
    [solve_case(i+1) for i in range(cases)]

if __name__ == '__main__':
    main()

