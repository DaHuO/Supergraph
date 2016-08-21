class LastWord:

    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        num_inputs = int(lines[0])
        outfile = open(filename + "_out", "w")
        for line_index in range(num_inputs):
            line = lines[line_index+1]
            result = LastWord.get_last_word(line)
            output = "Case #" + str(line_index+1) + ": " + str(result)
            print(line_index)
            outfile.write(output)

    @staticmethod
    def get_last_word(s):
        o = []
        for c in list(s):
            if len(o) == 0:
                o.append(c)
            else:
                if c >= o[0]:
                    o.insert(0, c)
                else:
                    o.append(c)
        return "".join(o)


if __name__ == '__main__':
    count = LastWord("A-large.in")
