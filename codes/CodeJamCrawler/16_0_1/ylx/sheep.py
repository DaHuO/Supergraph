from sys import *
f_i = open(argv[1])
f_o = open(argv[2], 'w')
cases = int(f_i.readline() [:-1])
for q in range(cases):
    header = 'Case #' + str(q+1) + ': '
    num = int(f_i.readline() [:-1])
    digits = []
    if num == 0:
        f_o.write(header + 'INSOMNIA\n')
    else:
        curr = num
        while True:
            curr_d = [d for d in str(curr)]
            for digit in curr_d:
                if digit not in digits:
                    digits.append(digit)
            if len(digits) > 9:
                f_o.write(header + str(curr) + '\n')
                break
            else:
                curr += num
f_o.close()
