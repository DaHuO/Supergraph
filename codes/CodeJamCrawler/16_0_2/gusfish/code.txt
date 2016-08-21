def g(liste):
    if liste == []: 
        return 0
    if len(liste) == 1:
        return 0
    else:
        if liste[-1] == liste[-2]:
            return g(liste[:-1])
        else: 
            return g(liste[:-1]) + 1

def h(liste):
    if liste[-1] == '+': 
        return g(liste)
    else: 
        return 1 + g(liste)


temp_res = []
with open("C:/Users/gus/Desktop/googlejam/pbm2/B-large.in") as input_file:
    for i, line in enumerate(input_file):
        if i==0:
            n = int(line)
        else:
            temp_res.append(line)
                
cases = []
for k, val in enumerate(temp_res):
    temp = []
    for char in val:
            if char == '+':
                    temp.append('+')
            elif char == '-':
                    temp.append('-')
    cases.append((k + 1, temp))


output_path = "C:/Users/gus/Desktop/googlejam/pbm2/B-large.out"

with open(output_path, mode='w') as output:
    for case in cases:
            answer = str(h(case[1]))
            output.write("Case #{i}: ".format(i=case[0]) + answer + '\n')