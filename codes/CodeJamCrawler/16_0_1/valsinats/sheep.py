file_in = "sheep.in"
file_out = "sheep.out"

def solve(N):
    if N == 0: return "INSOMNIA"

    seen = []
    for d in range(10): seen.append(0)

    i = 1

    while True:
        K = i * N

        for c in str(K):
            seen[ord(c) - ord('0')] = True

        if sum(seen) == 10:
            return K

        i = i + 1


with open(file_in) as fin, open(file_out, "w") as fout:
    T = int(fin.readline())

    for i in range(T):
        N = int(fin.readline())
        answer = solve(N)
        
        print("Case #{}: {}".format(i+1, answer), file=fout)

