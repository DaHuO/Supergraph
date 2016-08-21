def seen_all(list):
    for x in range(10):
        if x not in list:
            return False
    return True


reading_filename = "A-large.in"
writing_filename = "output.txt"


with open(reading_filename, "r") as file:
    contents = file.readlines()

with open(writing_filename, "w+") as file:
    tests = contents[0]
    print("Number of tests: {0}".format(tests))

    for case in range(1, int(tests)+1):
        n = int(contents[case])

        if n == 0:
            print("Case #{0}: INSOMNIA".format(str(case)))
            file.write("Case #{0}: INSOMNIA\n".format(str(case)))
            continue

        nums_seen = []

        i = 1
        while True:
            val = i * n

            for digit in str(val):
                nums_seen.append(int(digit))

            if seen_all(nums_seen):
                print("Case #{0}: {1}".format(str(case), str(val)))
                file.write("Case #{0}: {1}\n".format(str(case), str(val)))
                break

            i += 1
