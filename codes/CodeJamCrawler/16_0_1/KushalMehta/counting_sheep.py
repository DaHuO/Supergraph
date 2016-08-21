def all_same(items):
    return all(x == items[0] for x in items)

tc = int(input().strip())
numbers = [0,1,2,3,4,5,6,7,8,9]
for k in range(tc):
    numbers_match = [0,1,2,3,4,5,6,7,8,9]
    n = int(input().strip())
    if n == 0:
        print('Case #',k+1,': INSOMNIA',sep='')
        continue
    i=1
    n_new = n
    while(not all_same(numbers_match)):
        n_list = list(map(int,str(n_new)))
        if bool(set(n_list).intersection(numbers)):
            for j in range(len(n_list)):
                numbers_match[n_list[j]] = 1
        if not all_same(numbers_match):
            i+=1
            n_new = i*n
    print('Case #',k+1,': ',n_new,sep='')     
    