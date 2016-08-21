def reader(file):
    f_out = file[:-2]+"out"
    f = open(file)
    T = int(f.readline())
    cases = []
    for t in range(T):
        line = f.readline()
        if line[-1] == "\n":
            line = line[:-1]
        cases.append(line)
    return cases, f_out

# def solver(cases, f_out):
#     f_out = open(f_out,'w')
#     for c in range(len(cases)):
#         case = cases[c]
#         case_list = list(case)
#         y = 0
#         result = ''
#         for k in range(len(case_list)):
#             i = len(case) - k - 1
#             if case_list[i] == '-':
#                 y += 1
#                 if case_list[0] == '+':
#                     y += 1
#                     case_list[0] = '-'
#                 #flip
#                 case_list[:i+1] = case_list[:i+1][::-1]
#                 for j in range(i+1):
#                     if case_list[j] == '+':
#                         case_list[j] = '-'
#                     else:
#                         case_list[j] = '+'
#         print("Case #{}: {}".format(c+1,y), file=f_out)
#     f_out.close()

def solver(cases, f_out):
    f_out = open(f_out,'w')
    for c in range(len(cases)):
        case = cases[c]
        case_list = list(case)
        plus_number = 0
        minus_number = 0
        prev_sign = case_list[0]
        for m in case_list:
            if m != prev_sign:
                if m == '+':
                    minus_number += 1
                    prev_sign = '+'
                else:
                    plus_number += 1
                    prev_sign = '-'
        if case_list[-1] == '+':
            end = 0
        else:
            end = 1
        y = plus_number + minus_number + end
        print("Case #{}: {}".format(c + 1, y), file=f_out)
    f_out.close()



def main():
    cases, f_out = reader('B-large.in')
    solver(cases, f_out)

main()
