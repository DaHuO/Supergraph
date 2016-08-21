def run_code():
    t = int(input())

    res = []
    for i in range(t):
        numbers_seen = set([x for x in range(0,10)])
        n = int(input())

        prev_num = -1
        next_num = n
        counter = 1
        insomnia = False
        for digit in map(int, str(next_num)):
            if digit in numbers_seen:
                numbers_seen.remove(digit)

        while(numbers_seen):

            if prev_num == next_num:
                res.append([i+1, "INSOMNIA"])
                insomnia = True
                break

            prev_num = next_num
            counter += 1
            next_num = n * counter

            for digit in map(int, str(next_num)):
                if digit in numbers_seen:
                    numbers_seen.remove(digit)

                if (not numbers_seen):
                    break

        if not insomnia:
            res.append([i+1, next_num])

    for op in res:
        print("Case #" + str(op[0]) + ": " + str(op[1]))

if __name__ == "__main__":
    run_code()
