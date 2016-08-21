import sys
def read_content(lines_per_case):
    def detect_type(line):
        ca = [int(s) if s.isdigit() else s for s in line.split()]
        if len(ca) > 1:
            return ca
        else:
            return ca[0]
    with open(sys.argv[1],"r") as f:
        content = f.readlines()    
    inputs = [detect_type(c.rsplit('\n')[0]) for c in content] #convert string or int by datatype
    n = int(inputs[0])
    del inputs[0]
    test_cases = []
    for test in range(0,n*lines_per_case,lines_per_case):
        if lines_per_case > 1:
            cases = [[inputs[i]] if type(inputs[i]) != list else inputs[i] for i in range(test,test+lines_per_case)]
        else: cases = inputs[test]    
        test_cases.append(cases)
    return n, test_cases
n, content = read_content(1)
digits = [0,1,2,3,4,5,6,7,8,9]
msg = 0
f = open("A-large-out", "wb")
for case in range(n):
    init = content[case]
    nlist = []
    i = 1
    if init == 0: msg = "INSOMNIA"
    else:
        new_num = init
        while not all(x in nlist for x in digits):
            new_num = init * i
            for dgt in list(str(new_num)): 
                if dgt not in nlist : nlist.append(int(dgt))    
            i = i+1
        msg = new_num
    f.write("Case #{}: {} \n".format(case+1, msg))
f.close()
