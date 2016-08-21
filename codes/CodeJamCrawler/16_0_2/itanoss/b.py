import sys
def read(): return sys.stdin.readline().rstrip()

def convert(string):
    return int(string[::-1].replace('-', '1').replace('+', '0'), 2)

def calc(value):
    count = 0

    while value != 0:
        mask = (1 << value.bit_length()) - 1
        value = ~value & mask
        count += 1
    return count

T = int(sys.stdin.readline())

for t in range(T):
    value = convert(read())
    print("Case #{}: {}".format(t+1, calc(value)))