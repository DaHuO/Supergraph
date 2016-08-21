def digits(n): 
    if n<10: 
        return [n]
    else: 
        return digits(n/10)+ [n%10]

def digits(n): 
    if n<10: 
        return [n]
    else: 
        return digits(int(n/10))+ [int(n%10)]


def g(N): 
    if N==0: 
        return 'INSOMNIA'
    aux = set()
    i = 1
    while len(set(aux))<10:
        for digit in digits(i*N):
            aux.add(digit)
        i = i + 1
    return ((i-1)*N)

temp_res = []
with open("C:\Users\gus\Desktop\googlejam\A-large.in") as input_file:
    for i, line in enumerate(input_file):
        if i==0:
            n = int(line)
        else:
            temp_res.append(int(line))

cases = []
for k, val in enumerate(temp_res):
    cases.append((k + 1, val))
    
output_path = "C:\Users\gus\Desktop\googlejam\A-small.out"

with open(output_path, mode='w') as output:
    for case in cases:
            answer = str(g(case[1]))
            output.write("Case #{i}: ".format(i=case[0]) + answer + '\n')