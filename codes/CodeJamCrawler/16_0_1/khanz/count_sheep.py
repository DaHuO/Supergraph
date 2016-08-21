def count_sheep(N):
    if N == 0:
        return "INSOMNIA"
    counted = []
    i = 1
    while len(counted) != 10:
        num = str(N*i)
        for c in num:
            if c not in counted:
                counted.append(c)
        i += 1
    return N*(i-1)

def main():
    n = int(input())
    inputs = []
    for i in range(n):
        inputs.append(int(input()))
    for i in range(n):
        print('Case #{}: {}'.format(i+1, count_sheep(inputs[i])))
        
if __name__ == "__main__":
    main()
