import sys
import itertools

output_line = "Case #{X:d}: {flips:d}"

def flip(pancakes, end):
    for i in range(0, end):
        pancakes[i] = '-' if (pancakes[i] == '+') else '+'

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            pancakes = list(inhandle.readline().strip())
            # we could encode this as a bitvector but we'll skip this for code writing speed

            """print(pancakes)
            start, end = 0, len(pancakes)
            dir_end = True
            happy = '+'
            flips = 0
            while start < end:
                print(pancakes, start, end, happy)
                if dir_end:  # we're starting from end
                    print(pancakes[end - 1])
                    iend = end
                    while start < end and pancakes[end - 1] == happy:
                        end -= 1
                    if iend == end:
                        flips += 1
                    else:
                        happy = '-'
                    dir_end = False
                else:  # we're starting from front
                    istart = start
                    while start < end and pancakes[start] == happy:
                        start += 1
                    if istart == start:
                        flips += 1
                    else:
                        happy = '+'
                    flips += 1
                    dir_end = True"""
            end = len(pancakes)
            flips = 0
            while end:
                while end and pancakes[end - 1] == '+':
                    end -= 1
                flip(pancakes, end)
                flips += 1


            outline = output_line.format(X=t + 1, flips=flips - 1)
            print(outline, file=outhandle)
            print(outline)
