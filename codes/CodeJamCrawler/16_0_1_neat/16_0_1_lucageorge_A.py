f = open("OutputLarge.txt", "w")

def test(number, digits):
    current_digits = [int(x) for x in list(str(number))]
    for d in current_digits:
        if d in digits:
            digits.pop(digits.index(d))

    if digits:
        return True
    return False

i = 0
for N in open("A-large.in", "r"):
    if i != 0:
        N = int(N)

        if N == 0:
            ans = "Case #" + str(i) + ": " + "INSOMNIA\n"
        else:
            digits = list(range(10))
            iteration = 1
            
            while test(iteration * N, digits):
                iteration += 1
            
            ans = "Case #" + str(i) + ": " + str(iteration * N) + "\n"
        f.write(ans)
    i += 1
f.close()
