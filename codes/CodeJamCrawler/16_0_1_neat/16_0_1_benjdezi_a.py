samples = []

num_samples = int(raw_input())
for i in range(num_samples):
    samples.append(int(raw_input()))

for k in range(len(samples)):

    n = samples[k]

    if n == 0:
        print "Case #%s: INSOMNIA" % (k + 1)
    else:

        i = 0
        digits = [False] * 10
        num_seen = 0

        while True:
            i += 1
            p = i * n
            s = str(p)
            for d in s:
                if not digits[int(d)]:
                    num_seen += 1
                    digits[int(d)] = True
            if num_seen == len(digits):
                print "Case #%s: %s" % (k + 1, p)
                break
