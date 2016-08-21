f = open('data.in', 'r')
f2 = open('output.in', 'w')
nb = int(f.readline())
list_value = []
for i in range(nb):
    list_value.append(int(f.readline()))


print list_value

set_ref = set([0,1,2,3,4,5,6,7,8,9])
for idx,v in enumerate(list_value):
    set_nb = set()
    print('v:')
    print(v)
    if v == 0:
        f2.write('Case #{0}: {1} \n'.format(idx+1,'INSOMNIA') )
    else:
        multiple = 0
        while len(set_nb ^ set_ref) > 0:
            multiple += v
            copie = multiple
            #print multiple
            set_int =set()
            while copie:
                set_int = set_int | set([copie%10])
                copie = copie//10
            #print set_int
            #print set_nb
            set_nb = set_nb | set_int
        f2.write('Case #{0}: {1} \n'.format(idx+1,multiple) ) 



f.close()
f2.close()
    
