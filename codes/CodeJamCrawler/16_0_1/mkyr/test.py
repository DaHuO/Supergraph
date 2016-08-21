#!/usr/bin/python

debugging = 2

def log_me(level, st):
    global debugging
    if level >= debugging:
        print str(st)

def process_line(N):
    i_var = 1
    tmp_var = 0
    return_val = ''
    check_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        j_var = 0
        tmp_var = i_var * N
        i_var += 1
        str_var = str(tmp_var)
        while j_var < len(check_array):
            if check_array[j_var] in str_var:
                check_array.pop(j_var)
            else:
                j_var += 1

        if len(check_array) is 0:
            return_val = str(tmp_var)
            break

        if i_var > 1000:
            return_val = 'INSOMNIA'
            break

    print return_val
    return return_val

def main():
    inpt = open("C:/Users/tr1k3135/Downloads/A-small-attempt1.in", "r")
    onpt = open("C:/Users/tr1k3135/Downloads/small-practice.out", "w")

    T = int(inpt.readline().split()[0])
    for i in range(T):
        lines = []
        line = inpt.readline().split()
        N = int(line[0])
        cstr = "Case #%d:" % (i + 1)
        onpt.write(cstr + ' ' + process_line(N) + '\n')

    inpt.close()
    onpt.close()


if __name__ == "__main__":
    main()
