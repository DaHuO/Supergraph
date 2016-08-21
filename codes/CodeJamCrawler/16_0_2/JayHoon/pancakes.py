__author__ = 'jaehoonlee88'


#read_file = open('input', 'r')
read_file = open('B-large.in', 'r')
write_file = open('output', 'w')

num = int(read_file.readline())

for i in range(0, num):
    input_str = read_file.readline().rstrip('\n')
    token = list(input_str)
    count = 0
    prev = token[0]
    for j in range(1, len(token)):
        if prev != token[j]:
            count = count + 1

        prev = token[j]

    if token[-1] == '-':
        count = count + 1

    write_file.write("Case #" + str(i+1) + ": " + str(count) + '\n')



