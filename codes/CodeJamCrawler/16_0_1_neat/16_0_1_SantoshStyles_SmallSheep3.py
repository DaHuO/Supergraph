import os.path

with open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\input1.txt') as f:
    content = f.readlines()

f1=open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\output.txt', 'w+')

tEstCases = int(content[0])

for cases in range(1, tEstCases+1):

    nUmber = int(content[cases])

    iNdiv = []
    inSomnia= True

    for x in range(1, 100):
        mUlti = nUmber*x
        iNdiv.extend([int(i) for i in str(mUlti)])
        if 0 in iNdiv and 1 in iNdiv and 2 in iNdiv and 3 in iNdiv \
            and 4 in iNdiv and 5 in iNdiv and 6 in iNdiv and 7 in iNdiv \
            and 8 in iNdiv and 9 in iNdiv:
                f1.write('Case #'+str(cases)+': '+str(nUmber*x)+'\n')
                inSomnia= False
                break

    if inSomnia == True:
        f1.write('Case #'+str(cases)+': '+'INSOMNIA'+'\n')

f1.close()
