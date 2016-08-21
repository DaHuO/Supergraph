i_file = open("input.txt", "r")
o_file = open("output.txt", "w")

def check_set(s):
    for i in range(0, 10):
        if i not in s:
            return False
    return True

def add_digits(n, s):
    for ch in str(n):
        s.add(int(ch))

cases = int(i_file.readline().strip())
for case in range(cases):
    n = int(i_file.readline().strip())
    if n == 0:
        result = "Case #"+str(case+1)+": INSOMNIA\n"
        o_file.write(result)
        continue
    s = set()
    add_digits(n, s)
    counter = 2
    while check_set(s) == False:
        add_digits(n * counter, s)
        counter += 1
    result = "Case #"+str(case+1)+": "+str(n*(counter - 1))+"\n"
    o_file.write(result)

i_file.close()
o_file.close()