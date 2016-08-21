[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

for case in range(cases):
    # solving logic goes here
    letters = [x for x in raw_input().strip()]

    word = [letters[0]]
    letters.pop(0)

    while len(letters) > 0:
        # print word
        c = letters.pop(0)
        if ord(c) >= ord(word[0]):
            word = [c] + word
        else:
            word.append(c)

    # print and write output
    s = "Case #"+str(case+1)+": "+''.join(word)+'\n'
    out.write(s)
    print(s)
