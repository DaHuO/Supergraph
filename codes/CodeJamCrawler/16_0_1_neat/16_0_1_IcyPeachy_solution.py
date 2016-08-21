f = open("A-large.in", 'r')
cases = f.readline()
lines = f.readlines()
lines = list(map(int, lines))

def lastdreamnumber(a):
    if a == 0:
        return 'INSOMNIA'
    curr = a
    numbers = []
    check = [1,2,3,4,5,6,7,8,9,0]
    weight = 1
    while len(numbers) < 10:
        curr = curr * weight
        curr = ''.join(set(str(curr)))
        for i in curr:
            if i in numbers:
                qwokdpq = ''
            else:
                numbers.append(i)
        weight += 1
        curr = a
    return curr*(weight-1)
case = 1
for i in lines:
    out = open("output.txt", 'a')
    out.write("Case #"+str(case)+': '+str(lastdreamnumber(i))+'\n')
    out.close()
    case += 1
