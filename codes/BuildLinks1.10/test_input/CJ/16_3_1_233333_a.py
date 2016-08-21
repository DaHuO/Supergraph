import sys

def all_zero(items):
    return all(x == 0 for x in items)

input = sys.stdin.readlines()

for i in xrange(2,len(input),2):
    #print input[i]

    l = input[i].split()
    ans = 'Case #' + str(i/2)+': '+''
    l = map(int, l)

    if (len(l) == 2):
        while (not sum(l) == 0):
            if l[0] != l[1]:
                max_index = l.index(max(l))
                l[max_index] -= 1
                ans += chr(max_index + ord('A')) + ' '
            else:
                ans += 'AB '
                l[0] -= 1
                l[1] -= 1
        

    elif len(l) > 2:
        while (sum(l)>2):
            max_index = l.index(max(l))
            l[max_index] -= 1
            ans += chr(max_index + ord('A')) + ' '

        for j in xrange(len(l)):
            if l[j] >= 1:
                ans += chr(j + ord('A'))


    print ans.strip()
    #print l
