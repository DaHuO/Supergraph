fin = open("input.in", "r")
fw = open("output.out", "w")


num_to_letters = {
    '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7':'G', '8': 'H', '9': 'I', '10': 'J',
    '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S',
    '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'
}


t = int(fin.readline().rstrip())

for x in range(t):

    N = int(fin.readline())
    s = list(map(int, fin.readline().split()))
    result = []

    while(sum(s) > 2):
        m1 = max(s)
        ind1 = s.index(m1)
        s[ind1] -= 1
        m2 = max(s)
        ind2 = s.index(m2)
        s[ind2] -= 1

        flag = 1
        for i in range(len(s)):
            if s[i]+s[i] > sum(s):
                flag = 0
                break

        if(flag == 1):
            result.append(num_to_letters[str(ind1+1)] + num_to_letters[str(ind2+1)])
        else:
            s[ind2] += 1
            result.append(num_to_letters[str(ind1 + 1)])


    m1 = max(s)
    ind1 = s.index(m1)
    s[ind1] = 0
    m2 = max(s)
    ind2 = s.index(m2)
    result.append(num_to_letters[str(ind1 + 1)] + num_to_letters[str(ind2 + 1)])
    fw.write("Case #" + str(x + 1) + ": " + ' '.join(result) + "\n")

fin.close()
fw.close()