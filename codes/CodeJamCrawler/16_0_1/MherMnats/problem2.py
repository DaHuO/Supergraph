dict = {}
time = 100000

def check():
    for i in range(10):
        if not dict[i]:
            return False
    return True

def convertUpdate(n):
    string = str(n)
    for i in string:
        dict[int(i)] = True


def solve(n):
    global dict
    for i in range(10):
        dict[i] = False
    for i in range(1, time):
        convertUpdate(i*n)
        if check():
            return i*n
    return 'INSOMNIA'

input = open('A-large.in')
output = open('output.txt', 'w')
s = input.readline()
T = int(s)
for i in range(T):
    N = int(input.readline())
    result = "Case #{0}: ".format(i + 1) + str(solve(N)) + "\n"
    output.write(result)
