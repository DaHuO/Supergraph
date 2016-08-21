
def sleep_number(n):
    if n == 0:
        return "INSOMNIA"    
    s_ori = set(['0','1','2','3','4','5','6','7','8','9'])

    num = n
    while s_ori :
        s_n = set(list(str(num)))
        s_ori -= s_n
        num += n
    return num-n




file_in = open("A-large.in")
file_out = open('outputl.txt', 'w')

for line in file_in:
    case_number = int(line)
    break
cn = 1
for line in file_in:
    n = int(line)  
    # print n,sleep_number(n)
    file_out.write(
        'Case #'+str(cn)+': '+str(sleep_number(n))+'\n')
    cn += 1
file_out.close()