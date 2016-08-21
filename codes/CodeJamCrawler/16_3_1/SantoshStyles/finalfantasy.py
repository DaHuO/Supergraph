
with open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\A-large.in') as f:
    content = f.readlines()

f1=open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\outputSenate.txt', 'w+')

tEstCases = int(content[0])

def dostuff(mainnumber):
    part1 = int(mainnumber)*2
    part2=part1+1
    # print part2
    line1= content[part2-1].split()
    # print line1
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N' , 'O', 'P', 'Q', 'R', 'S' , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    box=[[]]
    for x in range(0, len(line1)):
        box[x]=[ letter[x]]*int(line1[x])
        box.append([])
    box.sort(key = len, reverse=True)
    del box[-1]
    collect=['']
    x=0
    print box

    while len(max(box, key=len))>0:
        if box[0]>0:
            while len(box)== 2 and len(box[0])==len(box[1]):
                print 'here'
                collect[x] += box[0].pop()
                box.sort(key = len, reverse=True)
                if not(bool(box[-1])):
                        del box[-1]
                collect[x] += box[0].pop()
                box.sort(key = len, reverse=True)
                if not(bool(box[-1])):
                        del box[-1]
                x=x+1
                collect.append('')
        # if len(box) == 2:
        #     collect[x] += box[0].pop()
        #     box.sort(key = len, reverse=True)
        #     if not(bool(box[-1])):
        #             del box[-1]
        #     print box
        #     collect[x] += box[0].pop()
        #     box.sort(key = len, reverse=True)
        #     if not(bool(box[-1])):
        #             del box[-1]
        #     print box
        #     break
        if not(bool(box)):
            break

        for y in range(1,2):
            if len(max(box, key=len))>0:
                collect[x] += box[0].pop()
                box.sort(key = len, reverse=True)
                if not(bool(box[-1])):
                    del box[-1]

        if bool(box) and len(box)>1:
            if len(max(box, key=len))>0 and len(box[0])>len(box[1]):
                collect[x] += box[0].pop()
                box.sort(key = len, reverse=True)
                if not(bool(box[-1])):
                        del box[-1]
        x=x+1
        #if len(max(box, key=len))== 2:

        if not(bool(box)):
            break
        collect.append('')
    print collect
    return collect



for cases in range(1, tEstCases+1):
    print cases
    answer = dostuff(cases)
    f1.write('Case #'+str(cases)+':')
    for z in answer:
        f1.write(' '+z)

    f1.write('\n')


# f1.close()