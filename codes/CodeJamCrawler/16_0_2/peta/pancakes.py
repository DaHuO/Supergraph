import sys
t = int(sys.stdin.readline())
for i in range(t):
    s = [letter for letter in sys.stdin.readline().strip()]
    tail = len(s)
    flips = 0
    while True:
        #print("".join(s))
        while s[tail - 1] == '+' and tail > 0: tail -= 1
        if tail == 0: break
        head = -1
        while s[head + 1] == '+' and head < tail: head += 1
        if head >= 0: flips += 1
        for j in range(head + 1, tail):
            s[j] = ('+', '-')[s[j] == '+']
        #print("HT", head, tail, "flipped", "".join(s))
        for j in range(tail//2):
            #print("swapping", j)
            s[j], s[tail-1-j] = s[tail-1-j], s[j]
        flips += 1
        #print("Flips ", flips)
    print("Case #" + str(i+1) + ": " + str(flips))


            

