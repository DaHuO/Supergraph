from sys import stdin, stdout
n = int(stdin.readline())
for j in range(1, n + 1):
    number = int(stdin.readline())
    s = set()
    i = 1
    while len(s) != 10 and number:
        s = s | set(list(str(number * i)))
        i += 1
    stdout.write('Case #' + str(j) + ': ')
    if not number:
        stdout.write('INSOMNIA' + '\n')
    else:
        stdout.write(str(((i - 1) * number)) + '\n')