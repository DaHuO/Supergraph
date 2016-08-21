def int_to_digits(n):
    n_str = str(n)
    return [int(x) for x in n_str]

def main():
    # read input
    test_cases = []
    T = input();
    for i in range(0,T):
        test_cases.append(int(input()))
    # test_cases = [0,1,2,11,1692]

    for i in range(0,len(test_cases)):
        N = test_cases[i]
        if N == 0:
            print("Case #" + str(i+1) + ": INSOMNIA")
            continue
        test = 0
        current = 0
        while test < 1023:
            current += N
            digits = int_to_digits(current)
            for d in digits:
                test |= 1 << d
        print("Case #" + str(i+1) + ": " + str(current))

main()
