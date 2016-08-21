cases = int(input())
def check_all_d(s):
    for i in range(10):
        if i not in s:
            return False
    return True
for i in range(cases):
    N = int(input())
    appeared = set()
    print("Case #{}: ".format(i+1), end="")
    if N == 0:
        print("INSOMNIA")
    else:
        multi = 1
        while True:
            for it in str(multi*N):
                appeared.add(int(it))
            if check_all_d(appeared):
                print(multi*N)
                break
            multi+=1
