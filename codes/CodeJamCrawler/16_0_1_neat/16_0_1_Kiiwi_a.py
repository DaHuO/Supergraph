file = open('A-large.in')
out = open('output.in', 'w')
T = int(file.readline().strip())
case = 1
for cases in range(T):
    input_line = file.readline().strip().split(" ")
    N = int(input_line[0])

    digit_list = []

    i = 1
    while len(digit_list) < 10:
        n = N*i
        if n == 0:
            n = 'INSOMNIA'
            break
        n_string = str(n)
        for digit in n_string:
            if digit not in digit_list:
                digit_list.append(digit)
            if len(digit_list) == 10:
                break
        i += 1
    out.write("Case #%i: %s\n" % (case, n))
    case += 1
