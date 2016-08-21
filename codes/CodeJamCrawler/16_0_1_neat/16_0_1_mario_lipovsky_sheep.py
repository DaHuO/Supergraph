def solve(N):
    digit_occurences = [0]*10

    def add_num(num):
        for d in str(num):
            digit_occurences[int(d)] += 1


    if N == 0:
        return "INSOMNIA"

    M = 0
    while 0 in digit_occurences:
        M += N
        add_num(M)
        
    return M 

T = int(input())

for t in range(T):
    print("Case #{}: {}".format(t+1, solve(int(input()))))

    