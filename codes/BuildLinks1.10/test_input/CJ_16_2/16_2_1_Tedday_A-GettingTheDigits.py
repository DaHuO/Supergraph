level = "A"
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
order = [0,6,4,2,5,7,8,3,1,9]


def test_case():
    counts = dict()
    for n in numbers:
        for letter in n:
            counts[letter] = 0
    for letter in input_file.readline().strip():
        counts[letter] +=1
    total = [0] * 10 
    for o in order:
        word = numbers[o]
        subtract = True
        for letter in word:
            if(counts[letter] == 0):
                subtract = False
        while(subtract):
            for letter in word:
                counts[letter] -= 1
                if(counts[letter] == 0):
                    subtract = False
            total[o] += 1
        
    return "".join([(str(i) * total[i]) for i in xrange(10)])
        

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
input_file.close()
output_file.close()
