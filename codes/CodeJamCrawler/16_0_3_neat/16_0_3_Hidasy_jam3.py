import sys
nl = sys.stdin.read().split()[1:]
n, j = [int(x) for x in nl]
print("Case #1:")
format_string = "1{0:0" + str(n-2) + "b}1"
increment_list = (format_string.format(i) for i in range(0, 2**n))
for _ in range(0, j):
    for candidate in increment_list:
        good = 0
        divisors = []
        for base in range(2, 11):
            bcandidate = int(candidate, base)
            good = 0
            for divisor in range(2, int(n**(1/2))+10):
                if bcandidate % divisor == 0:
                    good = 1
                    divisors.append(divisor)
                    break
            if good == 0:
                break
        if good == 1:
            break

    print(''.join(candidate), " ".join([str(x) for x in divisors]))
    
