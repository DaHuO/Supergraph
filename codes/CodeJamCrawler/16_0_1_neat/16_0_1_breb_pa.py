all_n = set([0,1,2,3,4,5,6,7,8,9])

def calculate():
    cases = int(input())
    for i in range(0, cases):
        ith_case_str = input()
        print("Case #{case}: {solution}".format(
            case = i+1,
            solution = solve(ith_case_str)
        ))

def solve(ith_case_str):
    if int(ith_case_str) == 0:
        return 'INSOMNIA'
    else:
        return rec_solve(set(), 1, ith_case_str)

def rec_solve(seen, mult, ith_case_str):
    numb = mult * int(ith_case_str)

    for ch in list(str(numb)):
        seen.add(int(ch))

    if seen == all_n:
        return (mult * int(ith_case_str))
    else:
        return rec_solve(seen, mult+1, ith_case_str)

calculate()