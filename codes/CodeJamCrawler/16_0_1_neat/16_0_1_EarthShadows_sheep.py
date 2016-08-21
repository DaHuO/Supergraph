
ALL = set(range(10))

def digitalize(number):
    ret = set()
    for char in str(number):
        ret.add(int(char))
    return ret

def do_print(case, number):
    out.write("Case #{0}: {1}\n".format(case, number))

f = open("A-large.in")
out = open("out.txt", "w")
T = int(f.readline())
print(T)

for i in range(T):
    N = int(f.readline())
    # print(N)

    digits = set()
    current = N
    while True:
        digits.update(digitalize(current))
        # print("Digits {0}".format(digits))
        if digits == ALL:
            do_print(i+1, current)
            break
        current = current + N
        if current == 0:
            do_print(i+1, "INSOMNIA")
            break

