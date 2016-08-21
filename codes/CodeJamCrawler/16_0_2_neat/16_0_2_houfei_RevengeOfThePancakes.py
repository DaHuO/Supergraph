def revenge_of_pancakes(stack_cake):
    check=list()
    flag=0
    for str_cake in stack_cake:
        if len(check)==0:
            check.append(str_cake)
            continue
        if str_cake!=check[len(check)-1]:
            flag=flag+1
            check.append(str_cake)
        else:
            check.append(str_cake)
            continue
    if check[len(check)-1]=='-':
        flag = flag + 1
    return flag



if __name__ == "__main__":
    fopen = open('test.in')
    output = open('output.txt', 'a')
    line_number = 0
    for lines in fopen:
        if (line_number == 0):
            line_number = line_number + 1
            continue
        character = lines.strip()
        output.write('Case #' + str(line_number) + ': ')
        output.write(str(revenge_of_pancakes(character)) + '\n')
        line_number = line_number + 1
    output.close()
