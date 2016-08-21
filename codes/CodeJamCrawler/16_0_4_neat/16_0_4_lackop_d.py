f = open('D-small.in', 'r')
out = open('D-small.txt', 'w')
T = int(f.readline())

for case in range(T):
    K, C, S = f.readline().strip().split()
    out.write("Case #" + str(case + 1) + ": " + " ".join(map(str, range(1, int(S) + 1))) + "\n")