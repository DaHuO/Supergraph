T = int(input().strip())
for test_case in range(1, T + 1):
    N = int(input().strip())
    if N == 0:
        num = "INSOMNIA"
    else:
        num = N
        digits = set(digit for digit in str(N))
        while len(digits) < 10:
            num += N
            digits.update(digit for digit in str(num))
    print("Case #{:d}: {}".format(test_case, num))
