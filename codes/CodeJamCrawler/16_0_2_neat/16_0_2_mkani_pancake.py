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
f = open("B-large-pan", "wb")
for p in range(n):
    cnt = 0
    new_pan = list(content[p])
    while '-' in new_pan:
        fir_pos = new_pan.index('-')
        if  fir_pos == 0:
            til_pos = new_pan.index('+') if '+' in new_pan else len(new_pan) 
            for i in range(til_pos): # flip over all the top '-' pancakes
                new_pan[i] = '+'
            cnt += 1
        else: 
            for i in range(fir_pos):
                new_pan[i] = '-'   #flip over all the top '+' pancakes
            cnt += 1
        #print new_pan     
    f.write("Case #{}: {}\n" .format(p+1, cnt))