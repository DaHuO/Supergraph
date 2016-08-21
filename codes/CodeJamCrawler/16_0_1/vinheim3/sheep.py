with open("A-large.in") as file:
    data = list(map(int, file.read().split('\n')[:-1]))

test_cases = data[0]

outfile = open("solution.txt", "w")

for i in range(test_cases):
    test_case = data[i+1]

    if test_case == 0:
        outfile.write("Case #{}: INSOMNIA\n".format(i+1))
        continue

    digits = [0]*10
    curr_multiple = test_case

    try:
        while True:
            x = curr_multiple
            
            while x != 0:
                digits[x % 10] = 1

                if sum(digits) == 10:
                    outfile.write("Case #{}: {}\n".format(i+1, curr_multiple))
                    raise "Break"

                x //= 10

            curr_multiple += test_case
    except Exception:
        pass

outfile.close()
quit()
