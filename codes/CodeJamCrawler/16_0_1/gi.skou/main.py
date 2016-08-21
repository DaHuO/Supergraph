from __future__ import print_function

with open('input', 'r') as f:
    count = int(f.readline())
    cases = [c.strip() for c in f.readlines()]
    for i in range(count):
        numbers = "0123456789"
        if i == 0:
            print("Case #{}: {}".format(i+1, "INSOMNIA"))
        else:
            case = cases[i]
            times = 1
            while True:
                times = times + 1
                for n in case:
                    numbers = numbers.replace(n, "")
                if not numbers:
                    print("Case #{}: {}".format(i+1, case))
                    break
                case = str(int(cases[i])*times)
