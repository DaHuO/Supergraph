f = open("OutputLarge.txt", "w")

i = 0
for S in open("A-large.in", "r"):
    if i != 0:
        S = S[:-1]

        word = S[0]
        for c in S[1:]:
            w1 = word + c
            w2 = c + word
            if w1 >= w2:
                word = w1
            else:
                word = w2
        
        print(word)
            
        ans = "Case #" + str(i) + ": " + str(word) + "\n"
        f.write(ans)
    i += 1
f.close()
