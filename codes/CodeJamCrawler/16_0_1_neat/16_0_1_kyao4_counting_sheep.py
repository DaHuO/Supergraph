"""
Created on Apr 8, 2016

@author: K.Yao
"""

if __name__ == '__main__':
    # read input
    with open('input.txt', 'rt') as fin:
        numCases = int(fin.readline())
        nList = []
        for i in range(numCases):
            nList.append(int(fin.readline()))

    outputString = ""
    for n, i in zip(nList, range(len(nList))):
        repeatTimes = 0

        numSet = set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
        allNum_flag = False
        count = 1
        last_numSet = set()
        cur_numSet = set()
        while repeatTimes <= 100 and not allNum_flag:
            cur_num = list(str(n * count))
            count += 1
            for digit in cur_num:
                cur_numSet.add(int(digit))
            if len(numSet.difference(cur_numSet)) == 0:
                allNum_flag = True
                continue
            if len(cur_numSet.difference(last_numSet)) == 0:
                repeatTimes += 1
            last_numSet = set(cur_numSet)
        if not allNum_flag:
            outputString += "Case #" + str(i + 1) + ": INSOMNIA" + "\n"
        else:
            outputString += "Case #" + str(i + 1) + ": " + "".join(cur_num) + "\n"

    fout = open('output.txt', 'wt', encoding = 'utf-8')
    fout.write(outputString)
    fout.close()


