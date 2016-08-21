from collections import namedtuple

Pancake = namedtuple("data", "indices")


class Pancakes:

    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        num_inputs = int(lines[0])
        outfile = open(filename + "_out", "w")
        for line_index in range(num_inputs):
            stack = lines[line_index+1]
            result = Pancakes.count_flips(stack)
            output = "Case #" + str(line_index+1) + ": " + str(result)
            print(line_index)
            outfile.write(output + "\n")

    @staticmethod
    def count_flips(pancake_stack):
        flips = 0
        pancake_array = list(pancake_stack)
        while pancake_array.count("-") != 0:
            i = 0
            while i + 1 < len(pancake_array) and (pancake_array[i+1] == pancake_array[i]):
                i += 1
            for j in range(i + 1):
                pancake_array[j] = Pancakes.flip_pancake(pancake_array[j])
            flips += 1
        return flips

    @staticmethod
    def flip_pancake(pancake):
        if pancake == "+":
            return "-"
        else:
            return "+"


if __name__ == '__main__':
    count = Pancakes("B-large.in")
