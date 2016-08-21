f = open('Input.txt', 'r')
num_tests = int(f.readline())
f2 = open('Output.txt', 'w')
for i in range(num_tests):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    multiplyer = 1
    n = int(f.readline())
    if n == 0:
        f2.write('Case #' + str(i + 1) +': INSOMNIA\n')

    else:
        while len(digits) > 0:
            n_str = str(n * multiplyer)
            for ch in n_str:
                if ch in digits:
                    digits.remove(ch)
            multiplyer += 1
        f2.write('Case #' + str(i + 1) + ': ' + n_str +'\n')
f.close()
f2.close()
