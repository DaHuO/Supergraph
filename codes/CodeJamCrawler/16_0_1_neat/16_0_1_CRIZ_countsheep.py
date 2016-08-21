__author__ = 'Christin'


def set_bit(v, index):
    return (v|(1<<index))

# t = int(input())

with open('A-large.in') as f:
    contents = f.readlines()


# inp = []
#
# for i in range(t):
#     val = int(input())
#     inp.append(val)

ans = []
contents = contents[1:]

for d in contents:
    d = int(d)
    i = int()
    i = 1
    flag = 0
    mas = 0

    if d == 0:
        ans.append("INSOMNIA")
        continue

    while True:
        val = int()
        an = int()
        val = i*d
        an = val
        i+=1

        while val != 0:
            x = val % 10
            #print(x)
            mas = set_bit(mas,x)
            if mas == 1023:
                #print("Here")
                ans.append(an)
                flag = 1
                break
            #print(mas)
            val/=10
            val = int(val)

        if flag == 1:
            break

count = 1
for d in ans:
    print("Case #"+str(count)+": "+str(d))
    count+=1







