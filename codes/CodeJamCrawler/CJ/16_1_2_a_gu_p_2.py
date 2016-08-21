in_file = open("B-large.in", "r")
out_file = open("out.txt", "w")
n_test_cases = int(in_file.readline().strip("\n"))
for test in range(n_test_cases):
    n = int(in_file.readline().strip("\n"))
    heights = {}
    for i in range(2 * n - 1):
        data = [int(i) for i in in_file.readline().strip("\n").split()]
        for height in data:
            if height not in heights:
                heights[height] = 1
            else:
                heights[height] += 1

    missing = []
    for height in heights:
        current = heights[height]
        if current % 2 != 0:
            missing.append(height)
    missing = [str(i) for i in sorted(missing)]

    out_file.write("Case #" + str(test + 1) + ": " + " ".join(missing) + ("\n" if test != n_test_cases - 1 else ""))
