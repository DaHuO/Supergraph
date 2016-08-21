f = open('test.txt','r')
data = f.readlines()
f.close()


def flip(l):
    global flips
    flips+=1
    pass

def toggle(l):
    v = l[0]
    av = "+" if v=='-' else "-"
    try:
        idx = l.index(av)
        toggle(l[idx:])
    except ValueError:
        pass
    flip(l)

flips = 0
def sort(l):
    l = list(reversed(l))
    global flips
    flips=0
    try:
        idx = l.index('-')
        toggle(l[idx:])
        return flips
    except ValueError:
        return flips

N = int(data[0])
i = 1
f = open("output.txt",'w')
for line in data[1:]:
    f.write("Case #%d: %d\n"%(i,sort(line.strip())))
    i+=1
f.close()
