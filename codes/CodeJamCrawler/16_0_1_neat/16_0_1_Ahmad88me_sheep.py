
def solve(case_no, f, fout):
    n = int(f.readline().strip())
    seen = [False, False, False, False, False, False, False, False, False, False]
    latest = None
    finished = False
    if n==0:
        fout.write("Case #"+str(case_no)+": "+"INSOMNIA"+"\n")
    for i in range(10000):
        if finished:
            # print latest
            # print seen
            fout.write("Case #"+str(case_no)+": "+str(latest)+"\n")
            return latest
        ds = (i+1) * int(n)
        # print ds
        for d in str(ds):
            dn = int(d)
            if not seen[dn]:
                seen[dn] = True
                latest = ds
                # print latest

        if i%10 == 0:
            finished = True
            for k in seen:
                if k == False:
                    finished = False
                    break


def main():
    f = open("input.txt", "r")
    fout = open("output.txt", "w")
    num_of_cases = int(f.readline().strip())
    # print num_of_cases
    for num in range(num_of_cases):
        solve(num+1, f, fout)
    f.close()
    fout.close()

main()