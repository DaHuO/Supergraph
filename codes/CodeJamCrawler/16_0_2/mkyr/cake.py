#!/usr/bin/python

def rollover(offset, length, arr):
    while offset < length:
        arr[offset] *= -1
        offset += 1


def process_line(line):
    no_operation = 0

    ## prepare array
    arr = []
    for ch in line:
        if ch is '-':
            arr.append(-1)
        elif ch is '+':
            arr.append(+1)

    arr.reverse()
    arr_length = len(arr)

    for index in range(arr_length):
        if arr[index] == -1:
            rollover(index, arr_length, arr)
            no_operation += 1

    print 'number of operations ', no_operation
    return str(no_operation)


def main():
    inpt = open("C:/Users/tr1k3135/Downloads/B-small-attempt0.in", "r")
    onpt = open("C:/Users/tr1k3135/Downloads/B-small-attempt0.out", "w")

    T = int(inpt.readline().split()[0])
    for i in range(T):
        line = inpt.readline().split()
        cstr = "Case #%d:" % (i + 1)
        onpt.write(cstr + ' ' + process_line(line[0]) + '\n')

    inpt.close()
    onpt.close()


if __name__ == "__main__":
    main()
