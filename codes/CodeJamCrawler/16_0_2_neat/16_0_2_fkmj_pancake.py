def work(c):
    st = raw_input().strip()
    o = ''
    counter = 0
    for s in st:
        if o != s:
            counter += 1
            o = s

    if st[-1] == '+':
        counter -= 1

    print ("Case #%d: %d" % (c,counter))

def main():
    t = int(raw_input())
    for i in range(t):
        work(i+1)

main()
