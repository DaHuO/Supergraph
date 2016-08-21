__author__ = 'Kirby'


def isComplete(digits):
    return len(digits) == 10

def output(results):
    fw = open("results.txt", "w")
    for i in range(len(results)):
        fw.write('Case #{:d}: {:s}\n'.format(i+1, results[i]))

if __name__ == "__main__":
    f = open("test.txt", "r")

    results = []

    T = int(f.readline())

    for i in range(T):
        digits = set()

        N = int(f.readline())

        if N == 0:
            results.append("INSOMNIA")

        else:
            num = 0
            while not isComplete(digits):
                num += N
                for d in str(num):
                    digits.add(d)

            results.append(str(num))

    output(results)








