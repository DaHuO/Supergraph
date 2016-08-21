#f = open('A-small-attempt0.in', 'r')
#g = open('A-small-attempt0.out', 'w')

#f = open('A-small.in', 'r')
#g = open('A-small.out', 'w')

f = open('A-large.in', 'r')
g = open('A-large.out', 'w')

for cases in range(int(f.readline())):
    line = f.readline()
    line = line[0:]
    
    final_word=''
    previous = ''
    
    final_word = line[0]
    if(line[1]>line[0]):
        final_word = line[1]+final_word
    else:
        final_word = final_word+line[1]
    
    for letters in line[2:]:
        first_letter = final_word[0]
        last_letter = final_word[-1]
        
        if(letters<first_letter):
            final_word = final_word + letters
        else:
            final_word = letters + final_word
        
        
    g.write("Case #"+str(cases+1)+": "+ final_word)
g.close()
