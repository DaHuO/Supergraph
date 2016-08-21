import os

def readfile(fname):
    with open(fname) as f:
        num_cases = int(f.readline())
        for line in f:
            try:
                sleep_cases.append(int(line))
            except ValueError:
                print('Done Reading')
    if len(sleep_cases) == num_cases:
        print("Correct Number Cases Loaded")
        return num_cases, sleep_cases

fname = 'A-large.in'
outfname = open('A-large.out','w')
sleep_cases = []
num_cases, sleep_cases = readfile(fname=fname)
case_result = ""
case_num = 0

for case in sleep_cases:
    if case == 0:
        case_result = "INSOMNIA"
    if case > 0:
        num_seen = []
        i = 0
        while len(num_seen) < 10:
            i += 1
            iter_case = case * i
            str_case = str(iter_case)
            for str_num in str_case:
                if str_num not in num_seen:
                    num_seen.append(str_num)
        case_result = str(iter_case)
    case_num +=1
    outfname.write("Case #" + str(case_num) + ": " + case_result+"\n")
    #outfname.write(os.linesep)