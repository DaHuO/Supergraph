import fileinput

def counting(n, case):
    if n == 0:
        return "Case #" + str(case) + ": INSOMNIA"
    else:
        counter = [0 for i in range(10)]
        num = 0;
        while 0 in counter:
            num += n
            curr = num
            while curr > 0:
                index = curr % 10
                if counter[index - 1] == 0:
                    counter[index - 1] = 1
                curr = curr / 10
        return "Case #" + str(case) + ": " + str(num)

if __name__ == '__main__':
    count = 0
    output = open('small_output.out', 'wb')
    for line in fileinput.input():
        if count != 0:
            output.write(counting(long(line), count) +"\n")
        count += 1
