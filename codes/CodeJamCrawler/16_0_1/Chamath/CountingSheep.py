__author__ = 'chamathsilva'

output = ''

def finder(number):
    if number == 0:
        return 'INSOMNIA'

    newNumber = number
    number_set = []
    count = 1
    while True:
        for i in list(str(newNumber)):
            if i not in number_set:
                number_set.append(i)

        if len(number_set) < 10:
            count += 1
            newNumber = count * number
        else:
            break

    return newNumber


for i in range(int(input())):
    output += "Case #"+str(i+1)+": "+str(finder(int(input())))+'\n'


print(output)

