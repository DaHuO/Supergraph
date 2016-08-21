def count_sheep(x):
    if x == 0: return "INSOMNIA"
    
    i = x
    lst = list(set(str(x)))
    
    while len(lst) < 10:
        i = i + x
        tmp = str(i)
        lst = list(set(lst + list(tmp)))
    return i

with open("input.in") as f:
    content = f.read().split('\n')

text_file = open("output.txt", "w")

for i in range(1, int(content[0])+1):
    n = count_sheep(int(content[i]))
    text_file.write("Case #{}: ".format(i) + str(n) + '\n')
    
text_file.close()