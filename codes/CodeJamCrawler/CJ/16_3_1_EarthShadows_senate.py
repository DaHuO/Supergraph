
f = open("A-large.in")
out = open("out.txt", "w")
T = int(f.readline())
print(T)

def calc_remain(d):
    sum = 0
    for (k, i) in d.items():
        sum += i
    return sum

for i in range(T):
    N = int(f.readline().strip())
    print(N)
    str = f.readline().strip().split()
    s = dict()
    for x in range(N):
        c = chr(ord('A') + x)
        s[c] = int(str[x])
    print(s)

    queue = ''
    while (calc_remain(s)):
        for x in range(N):
            c = chr(ord('A') + x)
            if s[c] > 0:
                queue+=c
                s[c] = s[c] -1
    print(queue)

    x = len(queue)-1
    new_queue = ''
    added = ''
    while x>=0:
        if x != 2:
            new_queue += queue[x] + queue[x-1] +' '
            x = x-2
        else:
            new_queue += queue[x] +' '
            x = x - 1
    new_queue = new_queue.strip()
    print("Case #{0}: {1}".format(i+1, new_queue))
    out.write("Case #{0}: {1}\n".format(i + 1, new_queue))