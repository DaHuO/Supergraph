x = input()
for i in range(int(x)):
    word = input()
    result = word[0]
    for j in range(1,len(word)):
        if word[j] >= result[0]:
            result = word[j] + result
        else:
            result = result + word[j]

    print("Case #",i+1,": ", result,sep='')
