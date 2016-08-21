i_file = open('A-large.in', 'r')
o_file = open('output.txt', 'w')

T = int(i_file.readline())
for t in range(T):
    N = int(i_file.readline())
    if N == 0:
        o_file.write("Case #" + str(t+1) + ": INSOMNIA" + "\n")
    else:
        seen = set()
        t_n = 0
        while len(seen) < 10:
            t_n += N
            t_s = str(t_n)
            for num in t_s:
                seen.update(num)
        o_file.write("Case #" + str(t+1) + ": " + str(t_n) + "\n")

i_file.close()
o_file.close()
