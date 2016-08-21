complete = set([0,1,2,3,4,5,6,7,8,9])

def solve(A):
    if A == 0:
        return 'INSOMNIA'
    A = int(A)
    current = set()
    iter = 1
    while(1):
        temp = A*iter
        while(temp>0):
            dig = int(temp%10)
            current.update([dig])
            temp //= 10

        if (current == complete):
            return A*iter
        else:
            iter += 1

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T+1):
        A = [int(x) for x in f.readline().split()]
        answer = solve(A[0])
        print("Case #{0}: {1}".format(case, answer))