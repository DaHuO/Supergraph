"""
Created on Apr 15, 2016

@author: K.Yao
"""


def findCombo(word, cur_word, resultList):
    if len(word) == 0:
        resultList.append(cur_word)
        return
    else:
        letter = word[0]
        new_word = list(word)
        del new_word[0]
        findCombo(new_word, letter + cur_word, resultList)
        findCombo(new_word, cur_word + letter, resultList)


def findCombo_wrapper(word, resultList):
    cur_word = ""
    findCombo(word, cur_word, resultList)


if __name__ == '__main__':
    # read input
    with open('input.txt', 'rt') as fin:
        numCases = int(fin.readline())
        words = []
        for i in range(numCases):
            words.append(fin.readline().strip())

    outputString = ""
    for word, i in zip(words, range(numCases)):
        resultList = []
        findCombo_wrapper(word, resultList)
        resultList.sort(reverse=True)
        outputString += "Case #" + str(i + 1) + ": " + resultList[0] + "\n"
    fout = open('output.txt', 'wt', encoding='utf-8')
    fout.write(outputString)
    fout.close()


