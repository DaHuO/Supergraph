
fh = open("input", "r")
file_content = []
fh.next()
for line in fh:
    file_content.append(line.strip())

print(file_content)
int_data = []
for s in file_content:
    int_data.append(int(s))
print(int_data)

fw = open("output", "w")

target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
case = 1
for N in int_data:
    seen_numbers = [] 
    print(N)
    i = 1
    N_mod = N
    if N_mod == 0:
        print "INSOMNIA"
        fw.write("Case #%s: INSOMNIA\n"%case)
        case += 1
        continue
    while seen_numbers != target:
        #print("seen numbers")
        #print(seen_numbers)
        for s in str(N_mod):
            seen_numbers.append(int(s))
        seen_numbers = list(set(seen_numbers))
        seen_numbers.sort()
        i += 1
        N_mod = N * i
    print("reached target")
    i = i - 1
    N_mod = N * i
    print N_mod
    
    fw.write("Case #%s: %s\n"%(case,N_mod))


    case += 1
fw.close()
