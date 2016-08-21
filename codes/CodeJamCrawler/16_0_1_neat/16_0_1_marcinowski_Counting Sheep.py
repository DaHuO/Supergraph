def reader(file):
    f = open(file,'r')
    f_out = file[:-2]+"out"
    T = int(f.readline())
    cases = []
    for t in range(T):
        line = int(f.readline())
        cases.append(line)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        numbers = ['0','1','2','3','4','5','6','7','8','9',]
        for N in range(1,10**6+1):
            case_iter = N*case
            case_str = str(case_iter)
            case_set = set()
            for i in case_str:
                case_set.add(i)
            for i in case_set:
                try:
                    while numbers.count(i) > 0:
                        numbers.remove(i)
                except:
                    continue
            if len(numbers) == 0:
                print("Case #{}: {}".format(c + 1, case_iter), file=f_out)
                break
        if len(numbers)>0:
            print("Case #{}: {}".format(c + 1, "INSOMNIA"), file=f_out)
    f_out.close()

def main():
    cases, f_out = reader('A-large.in')
    solver(cases, f_out)

main()


