import pdb;

def convert_symbols(symbols):
    pc_list = list()
    for letter in symbols:
        if letter == '+': pc_list.append(1)
        if letter == '-': pc_list.append(0)
    return pc_list

def switch(pc_list, n):
    new_list = list()
    for i in range(n-1,-1,-1):
#        pdb.set_trace()
        if pc_list[i] == 1: new_list.append(0)
        if pc_list[i] == 0: new_list.append(1)
    pc_list = new_list[:n] + pc_list[n:]
    return pc_list

def samesymbols(pc_list,i = 0):
    if i == len(pc_list) - 1: return len(pc_list)
    if pc_list[i+1] == pc_list[i]:
        return samesymbols(pc_list,i+1)
    else: return i+1

def sortpancackes(pc_list):
    flips = 0
    n = len(pc_list)
    for i in range(n,0,-1):
        #pdb.set_trace()
        if 0 not in pc_list: break
        if pc_list[i-1] == 1: continue
        if pc_list[0] == 1:
            pc_list = switch(pc_list,samesymbols(pc_list))
            flips += 1
        if 0 not in pc_list: break
        pc_list = switch(pc_list,i)
        flips += 1
    return flips

i = 0
f_read = open("symbols.txt")
f_write = open("Result_B_large.txt","w")
for line in f_read:
    if i == 0:
        i = 1
        continue
    f_write.write("Case #" + str(i) + ": " + str((sortpancackes(convert_symbols(line)))))
    f_write.write("\n")
    i += 1
