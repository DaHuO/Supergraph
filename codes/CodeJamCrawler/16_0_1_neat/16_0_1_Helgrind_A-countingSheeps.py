def splitting(N, seen):
    while(N > 0):
        seen[ N % 10 ] = True
        N //= 10
    return seen

def solve(N):
    seen = {}

    i = 0
    Nx = N
    while(len(seen) < 10):
        seen = splitting(Nx, seen)
        Nx += N
        i += 1

        if(i > 10000):
            return ('INSOMNIA')

    return Nx - N

# for _ in range(200+1):
#      print(_, solve(_))

for i,_ in enumerate(range(int(input()))):
    print('Case #{}: {}'.format(i+1, solve(int(input()))))