import pdb; #pdb.set_trace()

def mainfunc(members,n,i):
    remove_list = list()
    while sum(members)>0:
        max_list = [index for index,value in enumerate(members) if value == max(members)]
        if len(max_list) == 2:
            members[max_list[0]] -= 1
            members[max_list[1]] -= 1
            remove_list.append(''.join([chr(max_list[0] + ord('A')), chr(max_list[1] + ord('A'))]))
        else:# len(max_list) == 1:
            members[max_list[0]] -= 1
            remove_list.append(chr(max_list[0] + ord('A')))
    return "Case #" + str(i) + ": " + ' '.join(remove_list)




t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    members = [int(s) for s in raw_input().split(" ")]
    print mainfunc(members, n, i)
