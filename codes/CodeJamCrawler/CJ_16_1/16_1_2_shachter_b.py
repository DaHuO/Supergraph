import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    new_lines = []
    for line in lines:
        new_lines.append(line.split(' '))

    cur = 1


    for case in range(int(new_lines[0][0])):
        N = int(new_lines[cur][0])
        occur = {}
        for i in range(cur + 1, cur + 2*N):
            for height in new_lines[i]:
                if int(height) not in occur.keys():
                    occur[int(height)] = 1
                else:
                    occur[int(height)] += 1
        missing_h = []

        for key in occur.keys():
            if occur[key] % 2 == 1:
                missing_h.append(key)
        output0 = sorted(missing_h)
        output1 = []
        for q in output0:
            output1.append(str(q))

        output = ' '.join(output1)

        with open('output.txt', 'a') as ouput_file:
                ouput_file.write("Case #" + str(case + 1) + ": " + output + '\n')


        cur = 2*N + cur