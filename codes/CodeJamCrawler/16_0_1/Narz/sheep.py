import sys
def sheep(n):
    digits,counter= [],1
    if n <= 0:
        return "INSOMNIA"
    while len(digits) != 10:
        curr = n * counter
        [digits.append(d) for d in list(str(curr)) if d not in digits]
        counter+=1
    return curr
def format_file(filename):
    with open(filename) as f:
        out = open("output.txt","w+")
        for case,n in enumerate(f.readlines()[1:]):
            print("Case #{}: {}".format(case+1,sheep(int(n))),file=out)
        print("Done")
format_file(sys.argv[1])
