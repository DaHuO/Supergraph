def cat_last(lst = []):
    while(lst != [] and lst[lst.__len__() - 1] == '+'):
        lst.pop()
    return lst



def reverse_first(lst = []):
    lst_return = [0,0]
    i = 0
    count = 0
    while(lst[i] == '+'):
        lst[i] = '-'
        count += 1
        i += 1
    if(count != 0):
        lst_return[0] = 1
    lst_return[1] = lst
    return lst_return

def reverse_all(lst = []):
    lst.reverse()
    for i in range(lst.__len__()):
        if(lst[i] == '+'):
            lst[i] = '-'
        else:
            lst[i] = '+'
    return lst


inp= open('in2.txt', 'r')
a = inp.read().split('\n')
inp_list = [list(x) for x in a]

answer = 0
f = open("output2.txt", "w")
print(n)
for i in range(n):
    answer = 0
    while(inp_list[i] != []):
        inp_list[i] = cat_last(inp_list[i])
        if(inp_list[i] == []):
            break
        first = reverse_first(inp_list[i])
        if(first[0] != 0):
            answer += 1
        inp_list[i] = first[1]
        inp_list[i] = reverse_all(inp_list[i])
        answer += 1
    f.write("Case #" + str(i+1) + ": " + str(answer)+ "\n")

inp.close()
f.close()


