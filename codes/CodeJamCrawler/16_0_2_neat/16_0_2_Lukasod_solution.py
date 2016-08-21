def solution(case):
    n_flips = 0
    for i in range(len(case) - 1):
        if case[i] != case[i+1]:
            n_flips += 1
    if case[-1] == '-':
        return n_flips + 1
    else:
        return n_flips

T = int(input().strip())

for i in range(T):
    case = input().strip()
    print("Case #" + str(i+1) + ": " + str(solution(case)))
