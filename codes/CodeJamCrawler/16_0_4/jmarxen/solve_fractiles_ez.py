

num_cases = input()
cur_case = 1

while cur_case <= num_cases:
    kcs = raw_input().strip().split()
    s="Case #"
    s+=str(cur_case)
    s+=": "
    s2 = str(range(1,int(kcs[0])+1))
    #print s2
    s+=s2.replace("[","").replace("]","").replace(",", "")
    print s
    cur_case += 1