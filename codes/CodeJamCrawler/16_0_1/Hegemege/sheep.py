if __name__ == "__main__":
    f = open("in.txt", "r")
    data = f.readlines()
    f.close()

    f = open("out.txt", "w")

    data = [d.replace("\n", "") for d in data]



    for case in range(int(data[0])):
        n = int(data[1 + case])

        seen = [False for n in range(10)]

        iters = 0

        while True:

            for num in str(n):
                if not seen[int(num)]:
                    seen[int(num)] = True

            if sum(seen) == 10:
                f.write("Case #" + str(case + 1) + ": " + str(n) + "\n")
                break

            n += int(data[1 + case])

            iters += 1

            if iters > 10000:
                f.write("Case #" + str(case + 1) + ": INSOMNIA\n")
                break


    f.close()