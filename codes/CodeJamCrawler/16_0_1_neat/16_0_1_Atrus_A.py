def solve(N):
    if int(N) == 0:
        return "INSOMNIA"

    unique_digits = []
    counter = 0
    while len(unique_digits) < 10:
        counter+= 1
        num = str(counter * N)
        for digit in num:
            if digit not in unique_digits:
                unique_digits.append(digit)


    return counter * N


if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        cipher = int(input())
        print("Case #%i: %s" % (case_num, solve(cipher)))
