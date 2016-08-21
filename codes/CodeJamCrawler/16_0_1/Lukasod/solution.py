def add_new_numbers(N, arr):
    digits = [int(n) for n in str(N)]
    for i in digits:
        arr[i] = 1

def do_thing(N):
    if N == 0:
        return "INSOMNIA"
    seen_so_far = [0 for i in range(10)]
    i = 0
    while 0 in seen_so_far:
        i += 1
        add_new_numbers(i*N, seen_so_far)
    return i*N

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    print( "Case #"+ str(i+1) + ": " + str(do_thing(N)) )
