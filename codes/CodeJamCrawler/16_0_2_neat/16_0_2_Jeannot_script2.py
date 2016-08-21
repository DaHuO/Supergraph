def solve(input):
    nb_coups = 0
    while '-' in input:
         nb_coups += 1
         if input[0]=='+':
             pos = input.find("-")
         else:
             pos = input.rfind("-") + 1
         input = flip(input, pos)

    return nb_coups

def flip(str, N):
    inter_str = str[:N]
    inter_str = inter_str[::-1]
    
    ret_str = ''
    for index in range(N):
         ret_str += '+' if inter_str[index]=='-' else '-'
    return ret_str + str[N:] 


f = open("B-large.in") #Modifier fichier !!!
lines = f.readlines()
f.close()

tests_number = int(lines[0])
i = 1

f = open("output",'w+')
for line in lines[1:]:
    f.write("Case #{}: {}\n".format(i, solve(line)))
    i += 1

f.close()
