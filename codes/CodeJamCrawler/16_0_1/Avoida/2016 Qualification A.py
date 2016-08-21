def main():
    problem = open("A-large.in", "r")
    output = open("Problem-A-out.txt", "w")

    test = int(problem.readline().strip())

    for i in range(test):
        N = int(problem.readline().strip())
        current_seen = list()
        j = 0
        while len(current_seen) != 10:
            j += 1
            cur = N*j
            if j != 1 and cur == N:
                output.write("Case #" + str(i+1) + ": INSOMNIA\n")
                break
            while cur > 0:
                if cur % 10 not in current_seen:
                    current_seen.append(cur % 10)
                if len(current_seen) == 10:
                    output.write("Case #" + str(i+1) + ": " + str(N*j) + "\n")
                    break
                cur //= 10
    problem.close()
    output.close()

main()
