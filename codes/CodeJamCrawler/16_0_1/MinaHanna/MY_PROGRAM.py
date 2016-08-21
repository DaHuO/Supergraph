t = int(raw_input())
numbers = []
reference =  set('0123456789')
for i in range(1, t+1):
    numbers.append(raw_input())
for n in numbers:
    numset = set()
    for x in range (1,100):
        test = str(x*int(n))
        for ch in test:
            numset.add(ch)
        if (numset==reference):
            print 'Case #'+str(numbers.index(n)+1)+': '+ test
            break
    if (numset != reference):
        print 'Case #'+str(numbers.index(n)+1)+': INSOMNIA'

