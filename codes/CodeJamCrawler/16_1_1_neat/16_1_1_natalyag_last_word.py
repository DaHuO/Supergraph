
import sys
line_one = sys.stdin.readline()




for i in range(int(line_one)):
    line = sys.stdin.readline().strip()

    modified_line = line[0]
    for ch in range(1, len(line)):
        if line[ch] >= modified_line[0]:
            modified_line = line[ch] + modified_line
        else:
            modified_line += line[ch]
    print('Case #'+str(i + 1)+': '+ modified_line)





