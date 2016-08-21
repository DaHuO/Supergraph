import sys
import itertools

output_line = "Case #{X:d}: {answer}"


if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            N = int(inhandle.readline())

            if N != 0:
                seen = set()
                for multiple in itertools.count(1):
                    n = N * multiple
                    seen.update(str(n))
                    if len(seen) >= 10:
                        answer = n
                        break
            else:
                answer = 'INSOMNIA'

            outline = output_line.format(X=t + 1, answer=answer)
            print(outline, file=outhandle)
            print(outline)
