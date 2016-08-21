def sheep_counter(case, number):

    n = number
    bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def update(num):
        for j in str(num):
            bucket[int(j)] = 1

    def check():
        return bucket.__contains__(0)

    counter = 1
    flag = False
    while True:
        m = counter * n
        update(m)
        if not check():
            break
        counter += 1
        if (counter * n) == m:
            flag = True
            break
    if not flag:
        answer = "Case #"+str(case)+": " + str(counter * n)
    else:
        answer = "Case #"+str(case)+": INSOMNIA"
    return answer


f = open('A-small-attempt0.in', 'r')
w = open('out.txt', 'w')
i = 0
for line in f:
    if i:
        w.write(sheep_counter(i, int(line)) + "\n")
    i += 1
f.close()
w.close()
