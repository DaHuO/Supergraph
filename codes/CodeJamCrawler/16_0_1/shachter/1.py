import sys


if __name__ == "__main__":
    lines = []
    with open(sys.argv[1]) as f:
        lines0 = f.read().splitlines()
        for l in lines0:
            lines.append(int(l))

for d in range(1, lines[0]+1):
    i = 1
    dict = {}

    for a in range(10):
        dict[a] = 0
    while True:
        if lines[d] == 0:
            with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(d) + ": " + "INSOMNIA" + '\n')
            break
        for digit in str(lines[d]*i):
            dict[int(digit)] += 1

        if 0 not in dict.values():
            with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(d) + ": " + str(lines[d]*i) + '\n')
            break
        i += 1
