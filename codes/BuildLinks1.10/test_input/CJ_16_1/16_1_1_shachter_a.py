import string
import sys

if __name__ == "__main__":
    alphabet = list(string.ascii_uppercase)
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for case in range(int(lines[0])):

        output = ""
        for ch in lines[case+1]:
            if output == "":
                output = ch
            elif alphabet.index(ch) < alphabet.index(output[0]):
                output = output + ch
            else:
                output = ch + output
        with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(case + 1) + ": " + output + '\n')