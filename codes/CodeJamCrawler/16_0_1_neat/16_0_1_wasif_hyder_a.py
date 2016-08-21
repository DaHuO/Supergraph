def solution(num):
    i = 1
    result = ""
    if num == 0:
        return "INSOMNIA"
    while True:
        result = "".join(set(result + str(num * i)))
        if set(result) == set("1234567890"):
            return num*i
        i += 1



if __name__ == "__main__":
    with open("b.in", "r") as inp, open("bout.in", "w") as out:
        x = [int(line.strip()) for line in inp.readlines()]
        cases = x[0]
        x = x[1:]
        for case, num in enumerate(x):
            out.write("Case #{}: {}\n".format(case+1, solution(num)))

    # for i in range(10**6):
    #     print("Case #{}: {}".format(i, solution(i)))

