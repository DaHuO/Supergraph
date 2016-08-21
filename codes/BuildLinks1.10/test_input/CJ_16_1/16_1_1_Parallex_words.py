def sorter(word):
    words = [[word[0]]]
    for letter in word[1:]:
        aft = [x+[letter] for x in words]
        bef = [[letter] + x for x in words]
        words = bef + aft
    words = ["".join(x) for x in words]
    return sorted(words)[-1]

#content clear
with open("out.txt", "w") as file:
    pass


with open("A-small-attempt0.in", "r") as file:
    text = file.read()

text = text.splitlines()

#count = 0

tests = int(text[0])
for i in range(1, tests+1):

    #processing
    string = text[i]
    winning_word = sorter(string)
    

    #end processing
    
    with open("out.txt", "a") as file:
        
        file.write("Case #{}: ".format(i))
        # output
        file.write(winning_word)


        # end output
        file.write("\n")
        
        

    
    
    
