input_fp = open("sheep/A-large.in")
t = int(input_fp.readline())
with open("sheep/fuckthis.out", "w") as fp:
    for i in range(t):
        n = int(input_fp.readline())
        if n == 0:
            derp = i + 1
            fp.write("CASE #" + str(derp) + ": " +"INSOMNIA\n")
            continue

        digits_seen = [False] * 10
        digits_seen_count = 10

        a = n
        while digits_seen_count > 0:
            # find all the digits seen
            b = a
            while (b > 0):
                digit = b % 10
                b = b // 10
                if not digits_seen[digit]:
                    digits_seen[digit] = True
                    digits_seen_count -= 1

            if digits_seen_count == 0:
                break

            a += n
        c = i + 1
        fp.write("Case #"+str(c)+": " + str(a)+"\n")

    input_fp.close()