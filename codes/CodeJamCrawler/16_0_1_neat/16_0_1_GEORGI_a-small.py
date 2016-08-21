def bla(n, old_set={}, i = 1):
    #print(n, old_set, i)
    new_i = i+1
    new_digit = n*i
    new_set = {int(i) for i in str(new_digit)}
    u = new_set.union(old_set).union({int(i) for i in str(n)})
    if u == set([0,1,2,3,4,5,6,7,8,9]):
        #print(u)
        return new_digit
    return bla(n=n, old_set=u, i=new_i)

def func(n):
    if n == 0:
        return 'INSOMNIA'
    if n == 1234567890:
        return n
    return bla(n)

with open('A-large.in.txt', 'r') as infile:
    for place, line in enumerate(infile):
        if place:
            n = int(line)
            result = func(n)
            if result == 'INSOMNIA':
                print("Case #%d: INSOMNIA" % place)
            else:
                print("Case #%d: %d" % (place, result))

