#!/usr/bin/python3


def get_output(input_val):
    if input_val == 0:
        return "INSOMNIA"
    current_count = input_val
    numbers = set(str(input_val))
    while 1:
        current_count += input_val
        numbers.update(list(str(current_count)))
        if len(numbers) == 10:
            return current_count

if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, get_output(int(input()))))
