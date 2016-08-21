import string

letters = string.ascii_letters.upper()



def solve(numb,people):
    last, membs = lastTwo(people)
    if last:
        return letters[membs[0]] + letters[membs[1]]
    else:
        a = max(people)
        count = 0
        m = []
        for i in range(len(people)):
            if people[i] == a:
                count +=1
                m.append(i)
        if count == 1:
            people[m[0]] = people[m[0]] - 2
            return letters[m[0]]+letters[m[0]]  + ' ' + solve(numb, people)
        elif count % 2 == 1:
            people[m[0]] = people[m[0]] - 1
            return letters[m[0]] + ' ' + solve(numb, people)
        else: 
            people[m[0]] = people[m[0]] - 1
            people[m[1]] = people[m[1]] - 1
            return letters[m[0]] + letters[m[1]] + ' ' + solve(numb, people)              
    



def lastTwo(people):
    count = 0
    membs = []
    x = max(people)
    if not x == 1:
        return (False, [])
    else:
        for i in range(len(people)):
            if people[i] == 1:
                count +=1
                membs.append(i)
        return (count == 2, membs)



f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    numb = int(f.readline().split('\n')[0])
    people = f.readline().split('\n')[0].split(' ')
    people = [int(x) for x in people]

    #solve
    ans = solve(numb, people)
    pr = "Case #"+str(i)+ ": " + str(ans)
    print pr
    g.write(pr + '\n')


f.close()
g.close()
