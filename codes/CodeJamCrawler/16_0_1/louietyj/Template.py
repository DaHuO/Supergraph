with open('A-large.in', 'r') as f:
    data = f.read()

data = data.split('\n')
output = []

def fn(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        digits = set(range(10))
        next_n = n
        while True:
            for digit in map(int, str(next_n)):
                if digit in digits:
                    digits.remove(digit)
            if len(digits) == 0:
                return next_n
            next_n += n

print(data.pop(0), 'cases.\n')
while data:
    if data[0] == '':
        break
    n = int(data.pop(0))
    output.append(fn(n))

with open('submission.txt', 'w+') as f:
    i = -1
    for i, answer in enumerate(output):
        f.write("Case #%i: %s\n" % (i+1, answer))
        print("Case #%i: %s" % (i+1, answer))
    print('\n%i cases written to file' % (i+1))
