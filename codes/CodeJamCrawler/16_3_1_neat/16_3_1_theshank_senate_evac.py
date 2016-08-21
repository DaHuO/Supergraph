from sys import stdin, stdout
import time

alp = [-1] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if __name__ == "__main__":
    t = int(stdin.readline().strip())
    for cno in range(1, t + 1):
        n = int(stdin.readline().strip())   # parties are from alp[1:n+1]
        # print("n", n)
        p = [int(v) for v in stdin.readline().strip().split(" ")]
        # print("p", p)
        m = sum(p)  # number of members left in the senate
        # print("m", m)
        counts = list(zip(alp[1:n + 1], p))
        # print("counts", counts)
        res = []

        while m > 0:
            # when the control reaches here, we have the top 2 counts equal
            # remove one from the largest
            if len(counts) > 2:
                # sort counts by number of members left
                counts.sort(key=lambda tup: tup[1])
                while counts[-1][1] > counts[-2][1]:
                    res.append(counts[-1][0])
                    counts[-1] = (counts[-1][0], counts[-1][1] - 1)
                    m -= 1
                res.append(counts[-1][0])
                counts[-1] = (counts[-1][0], counts[-1][1] - 1)
                m -= 1
                if counts[-1][1] == 0:
                    counts = counts[:-1]
            else:
                # only two parties remain and they have the same strength
                res.append(counts[0][0] + counts[1][0])
                m -= 2
                # print(res)

            # print(res)
        print("Case #{}: {}".format(str(cno), " ".join(res)))
