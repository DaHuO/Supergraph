numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open("A-large.in.txt") as f:
    m = f.readlines()
f.close()
f = open('output.txt','w')
j = 0
for row in m[1:]:
    j += 1
    number_buffer = numbers
    value = int(''.join(row))
    i = 1
    if value == 0:
        f.write("Case #{}: INSOMNIA\n".format(j))
        continue
    else:
        while len(number_buffer):
            number_buffer = list(filter(lambda x: x not in str(value * i), number_buffer))
            i += 1
        f.write("Case #{}: {}\n".format(j, value*(i-1)))
