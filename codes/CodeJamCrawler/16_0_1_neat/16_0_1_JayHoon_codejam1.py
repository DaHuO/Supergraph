__author__ = 'jaehoonlee88'


input_file = open('A-large.in', "r")
output_file = open('output.txt', "w")

T = int(input_file.readline())

def update(lst, number):
    count = 0
    while number > 0:
        if lst[number % 10] == False:
            lst[number % 10] = True
            count = count + 1

        number = number / 10
    return count

input_data = []
for i in range(0, T):
    N = int(input_file.readline())
    input_data.append(N)

for i in range(0, T):
    N = input_data[i]
    count = 0
    lst = [False for j in range(10)]

    line_cha = ''
    if i != (T-1):
        line_cha = '\n'

    if N == 0:
        output_file.write("Case #" + str(i+1) + ": " + "INSOMNIA" + line_cha)
    else:
        N_add = 0
        while count != 10:
            N_add = N_add + N
            count += update(lst, N_add)

        output_file.write("Case #" + str(i+1) + ": " + str(N_add) + line_cha)

input_file.close()
output_file.close()


