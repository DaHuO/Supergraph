from sys import stdout
import queue as queue

T = int(input())

for t in range(1, T+1):
    stdout.write("Case #"+str(t)+": ")

    N = int(input())
    parties = [[int(x), chr(int(i)+ord("A"))] for i, x in enumerate(str(input()).split())]
    parties.sort()
    parties = list(reversed(parties))

    q = queue.Queue()
    for p in parties:
        q.put(p)

    stack = []
    while q.qsize() > 0:
        s = ""
        for i in range(2):
            if not q.empty():
                p = q.get()
                p[0] = p[0] - 1
                s += p[1]
                if p[0] > 0:
                    q.put(p)
        stack.append(s)

    while len(stack) > 0:
        stdout.write(stack.pop())
        if len(stack) != 0:
            stdout.write(" ")
    stdout.write("\n")

