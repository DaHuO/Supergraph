def reader(file):
    f_out = file[:-2] + 'out'
    f = open(file,'r')
    T = int(f.readline())
    cases = []
    for t in range(T):
        KCS = f.readline()
        KCS_list = KCS.split(' ')
        cases.append(KCS_list)
    return cases, f_out

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        K = int(case[0])    
        C = int(case[1])
        result = [i*K**(C-1)+1 for i in range(K)]
        #ZAMIENIC RESULT W STRINGA
        string = ''
        for i in result:
            string += str(i) + ' '
        print("Case #{}: {}".format(c + 1, string), file = f_out)
    f_out.close()

def main():
    cases, f_out = reader('D-small-attempt0.in')
    solver(cases, f_out)
    
main()
