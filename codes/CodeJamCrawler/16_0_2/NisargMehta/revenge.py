def rev(n):
    if(n == '-'):
        return '+'
    else:
        return '-'
tc = int(input())
for i in range(tc):
    ip = input()
    ip_list = []
    con = 0
    con_max = 0
    char_max = ''
    ip_list.append(ip[0])
    prev = ip[0]
    total_moves = 0
    for char in ip[1:]:
        ip_list.append(char)
        if(char == prev):
            con += 1
        else:
            if(con > con_max):
                con_max = con
                char_max = prev
                prev = char
    while '-' in ip_list:
        if('+' not in ip_list):
            total_moves += 1
            break
        if(ip_list[0] != ip_list[1]):
            ip_list[0] = ip_list[1]
            total_moves += 1
        if(rev(ip_list[0]) in ip_list):
            first_rev = ip_list.index(rev(ip_list[0]))
        else:
            if('-' in ip_list):
                total_moves += 1
            break
        index = 0
        while(index < first_rev):
            ip_list[index] = rev(ip_list[index])
            index += 1
        total_moves += 1
    print("Case #"+str(i+1)+": "+str(total_moves))
