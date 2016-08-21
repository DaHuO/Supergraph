def contains_zeros(num_list):
    for num in num_list:
        if num == 0:
            return True
    return False
directory = '/Users/jeremiahsimmons/Desktop/'
in_file = open(directory + 'input.txt')
out_file = open(directory + 'output.txt', 'w')

num = int(in_file.readline())

for times in range(1, num + 1):
    occur = [0]*10
    i = 1
    curr_num = int(in_file.readline())
    if curr_num == 0:
        out_file.write('Case #' + str(times) + ': INSOMNIA\n')
    else:
        while contains_zeros(occur):
            multiple = curr_num * i
            for dig in str(multiple):
                occur[int(dig)] += 1
            i += 1
        out_file.write('Case #' + str(times) + ': ' + str(multiple) + '\n')

in_file.close()
out_file.close()