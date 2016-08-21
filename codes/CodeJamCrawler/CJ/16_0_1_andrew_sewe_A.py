file = "A-large"
with open(file + ".in") as f:
    content = [line.rstrip('\n') for line in open(file + ".in")]
text_file = open(file + ".out", "w")

for index in range(len(content)):
    lastNumber = ""
    if index > 0 :
       print ("Case #" + str(index))
       n = int(content[index])
       if n == 0 :
           #print ("INSOMNIA")
           lastNumber = "INSOMNIA"
       else :
            numbers = "1234567890"
            
            i = 1
            while numbers != "" :
                #print ("digits left: " + numbers)
                current = str(i * n)
                lastNumber = current
                for letter in current :
                    if numbers.find(letter) != -1 :
                        numbers = numbers.replace(letter, "")
                        #print ("digit removed: " + letter)
                i = int(i) + 1
       #print ("last Number: " + lastNumber)                 
       text_file.write("Case #" + str(index) + ": " + lastNumber + "\n")
       lastNumber = ""
                 
    print ()
text_file.close()
