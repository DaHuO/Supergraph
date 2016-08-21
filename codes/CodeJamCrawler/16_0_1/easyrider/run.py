#!/usr/bin/python
from __future__ import print_function


nr_of_tasks = int(raw_input())
numbers = [0]*10

def init():
    global numbers
    numbers = [0]*10
    return


def read_line():
    return raw_input()

def read_line_int():
    return int(raw_input())


def split_number(input):
    global numbers
    nums = str(input)
    for num in nums:
        numbers[int(num)] = 1



def check():
    global numbers
    if sum(numbers) == 10:
        return True
    else:
        return False





def main():
    global numbers, nr_of_tasks
    for i in range(1,nr_of_tasks+1):
        init()
        start_value = abs(read_line_int())
        value = start_value
        if value is not 0:
            split_number(value)
            if not check():
                for mult in range(1,100000):
                    value = value + start_value
                    split_number(value)
                    if check():
                        result = value
                        break
                    if mult == 9999:
                        result = "INSOMNIA2"

            else:
                result = value
        else:
            result = "INSOMNIA"

        print("Case #{task}: {result}".format(task=i,
                                 result=str(result)))

if __name__ == "__main__":
    init()
    main()


