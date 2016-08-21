f = open('input.in', 'r')
f.readline()
case = 1
while True:
    string = f.readline()
    string = string.rstrip()
    if string == '':
        break
    string = list(string)
    index = {'+':1, '-':-1}
    for i in range(len(string)):
        string[i] = index[string[i]]

    fliptimes = 0
    while True:
        if sum(string) == len(string):
            break
        counter = len(string)
        for i in range(len(string)):
            if abs(sum(string[:i+1])) != i+1:
                counter = i
                break
                
        for i in range(len(string[:counter])):
            string[i] *= -1
        fliptimes += 1

    print("Case #%d:"%case,fliptimes)
    case += 1
