# Read linescount
t = int(input())
for i in range(1, t + 1):
    num = int(input())
    digits = [False, False, False, False, False, False, False, False, False, False]
    # Actual calculating start
    if(num == 0):
        print("Case #{}: {}".format(i, "INSOMNIA"))
    else:
        # Do more calculating here
        multi = 1
        n = 0
        while n == 0:
            result = num * multi
            multi += 1
            found_digits = [int(j) for j in str(result)]
            for digit in found_digits:
                digits[int(digit)] = True
            for digit in digits:
                if digit == True:
                    n = result
                else:
                    n = 0
                    break
        # Actual calculating stop
        print("Case #{}: {}".format(i, n))
