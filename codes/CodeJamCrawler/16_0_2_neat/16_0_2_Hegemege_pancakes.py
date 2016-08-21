if __name__ == "__main__":
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    f = open("out.txt", "w")

    data = [d.replace("\n", "") for d in data]



    for case in range(int(data[0])):
        stack = [data[1 + case][i] == "+" for i in range(len(data[1 + case]))]

        running = stack[0]
        flips = 0
        for i in range(len(stack)):
            if running == stack[i]:
                continue

            top = stack[:i]
            top = [not item for item in top][::-1]

            stack = top + stack[i:]
            running = not running

            flips += 1

        if running == False:
            flips += 1

        f.write("Case #" + str(case + 1) + ": " + str(flips) + "\n")


    f.close()