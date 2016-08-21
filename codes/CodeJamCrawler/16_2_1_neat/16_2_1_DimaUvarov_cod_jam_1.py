inp= open('in1.txt', 'r')
inp_list = [int(x) for x in inp.read().split('\n')]

n = inp_list.pop(0)
num = set()
answer = []
f = open("output1.txt", "w")

def to_num(a):
    a = str(a)
    result = set()
    for i in a:
        result.add(i)
    return set(result)

for i in range(n):
    cur = set()
    if((inp_list[i]) == 0):
        f.write("Case #" + str(i+1) + ": INSOMNIA" + "\n")
    else:
        for j in range(1,1000000000):
            cur.update(to_num(j*inp_list[i]))
            # print(cur)
            if(cur.__len__() == 10):
                f.write("Case #" + str(i+1) + ": " + str(j*inp_list[i])+ "\n")
                break
inp.close()
f.close()
