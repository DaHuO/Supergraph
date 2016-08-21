# digits = [False] * 10
# print digits



def get_digits(number):
    t = list()
    if number == 0:
        t.append(number)
    while number != 0:
        digit = number % 10
        number = number / 10
        if digit not in t and digit != None:
            t.append(digit)
    return t

with open("A-small-attempt0.in") as f:
    content = f.readlines()

cases = int(content[0])

for i in range(1,cases + 1):
    digitss = list()
    number = int(content[i])
    iteration = 1
    asleep = False

    while len(digitss) < 10:
        digs = get_digits(iteration * number)
        for dig in digs:
            if dig not in digitss:
                digitss.append(dig)

        iteration += 1

        if iteration > 200000:
            asleep = True
            break

    if asleep == True:
        print "Case #%d: %s"%(i, "INSOMNIA")
    else:

        print "Case #%d: %d"%(i, (iteration - 1) * number)
