
def bleatrix(n, h):
    if (n == 0):
        return 'INSOMNIA'
    count = 0
    while not len(h) == 0:
        count += 1
        temp = n * count
        for digit in str(temp):
            if digit in h:
                h.remove(digit)
    return n * count

testcases = 0
output = open('output.txt', 'w')
with open('input.txt', 'r') as f:
    testcases = int(f.readline())
    count = 0
    for line in f:
        count += 1
        h = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
        output.write("CASE #" + str(count) + ': ' + str(bleatrix(int(line), h)) + '\n')

output.close()