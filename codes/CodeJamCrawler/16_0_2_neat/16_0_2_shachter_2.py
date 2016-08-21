import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    for case in range(int(lines[0])):
        flips = 0
        side = '+'
        for ch in range(len(lines[case+1])):
            if lines[case+1][len(lines[case+1]) - ch - 1] != side:
                flips += 1
                side = lines[case+1][len(lines[case+1]) - ch - 1]
        with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(case + 1) + ": " + str(flips) + '\n')
