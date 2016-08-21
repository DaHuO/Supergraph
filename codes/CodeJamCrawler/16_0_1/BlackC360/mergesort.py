f = open('Sheep.txt', 'r')

output = ""


for i in range(int(f.readline())):
    n = int(f.readline())

    if n ==  0:
        result = "INSOMNIA"
    else:
        figures = []
        o = 0
        while len(figures)<10:
            o = o+n
            result = o
            for a in str(o):
                if int(a) not in figures:
                    figures.append(int(a))
            
            

    output += "Case #" + str(i+1) + ": " + str(result) + "\n"


print(output)
