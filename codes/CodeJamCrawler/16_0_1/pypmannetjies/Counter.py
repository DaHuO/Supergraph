class Counter:

    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        num_inputs = int(lines[0])
        outfile = open(filename + "_out", "w")
        for line_index in range(num_inputs):
            start = int(lines[line_index+1])
            result = Counter.count_sheep(start)
            output = "Case #" + str(line_index+1) + ": " + str(result)
            outfile.write(output + "\n")

    @staticmethod
    def count_sheep(start):
        if start == 0:
            return "INSOMNIA"
        else:
            digits = [False] * 10
            i = 1
            while True:
                n = start * i
                i += 1
                n_string = str(n)
                for digit in n_string:
                    digits[int(digit)] = True
                if digits.count(False) == 0:
                    return n


if __name__ == '__main__':
    count = Counter("A-large.in")