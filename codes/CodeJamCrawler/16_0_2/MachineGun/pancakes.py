import sys

number_of_cases = int(sys.stdin.readline().strip())

for case in range(number_of_cases):
    operations = 0
    return_line = "Case #"+str(case+1)+": "
    cakes = sys.stdin.readline().strip()
    list_of_chars = list(cakes)
    list_of_chars.reverse()
    #print list_of_chars
    while any(c=='-' for c in list_of_chars):
        #do revange
        operations += 1
        for index in range(list_of_chars.index('-'), len(list_of_chars)):
            if list_of_chars[index] == '-':
                list_of_chars[index] = '+'
            else:
                list_of_chars[index] = '-'

    else:
        print(return_line + str(operations))
