t = int(input())

output = open("output.txt", "w")


for i in range(1, t +1):
    n = int(input())
    digitsRemaining = ["0","1","2","3","4","5","6","7","8","9"]
    j = 1
    last = 0

    while len(digitsRemaining) != 0:
        m = str(n*j)
        
        if m == "0":
            last = "INSOMNIA"
            break

        for digit in m:
            if digit in digitsRemaining:
                    position = digitsRemaining.index(digit)
                    digitsRemaining = digitsRemaining[:position] + digitsRemaining[position+1:]

                
        last = m
        j += 1
    output.write("Case #{}: {}\n".format(i, last))
    
output.close()
