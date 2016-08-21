__author__ = 'ThomasRiley'

with open('input.txt') as f:
    testCases = f.readlines()
    n = testCases[0]
    for i in range(1, int(n)+1):
        s = set()
        num = (int(testCases[i]))
        done = False
        x = 1
        while not done:
            if num == 0:
                print('Case #'+str(i)+': INSOMNIA')
                done = True
            #if str(num) not in s:
             #   s.add(str(num))
            for c in str(num*x):
                s.add(c)

            if len(s) == 10:
                print('Case #'+str(i)+': '+str(num*x))
                done = True
            x += 1