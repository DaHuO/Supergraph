def read_file():
    f = open("B-large.in", 'r')
    num_case = int(f.readline())

    for n in range(num_case):
        string = list(f.readline()[::-1])
        len_str = len(string)
        count = 0

        for i in range(len_str):
            if string[i] == '-':
                string[i] = flip(string[i])
                count +=1
                for j in range(len_str-(i+1)):
                    string[j+i+1] = flip(string[j+i+1])

        print_result(n+1, count)

def flip(c):
    if c == '-':
        return '+'
    elif c == '+':
        return '-'
    else:
        return c

def print_result(case, last_num):
    print('Case #{}: {}'.format(case,last_num))    

read_file()