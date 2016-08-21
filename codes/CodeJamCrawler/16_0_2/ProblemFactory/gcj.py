def pancakes(setup):
    if setup == '+': return 0
    if setup == '-': return 1
    index, count = 0, 0
    while (1):
        if setup[index] == '+':
            while(index < len(setup) and setup[index] == '+'):
                index+=1
                if index == len(setup):
                    return count
            count += 1
            
            while(index < len(setup) and setup[index] == '-'):
                index += 1
                if (index == len(setup)):
                    return count + 1
            count += 1
        else:
            if setup[index] == '-':
                while(index < len(setup) and setup[index] == '-'):
                    index += 1
                if (index == len(setup)):
                    return count + 1
            count += 1
            while(index < len(setup) and setup[index] == '+'):
                index+=1
                if index == len(setup):
                    return count
            count += 1
            
            
if __name__ == "__main__":
    output = open("output.txt","w")
    with open("input.txt") as f:
        num =int(f.readline())
        for i in range(num):
            setup = f.readline().strip()
            output.write("Case #" + str(i+1) + ": " + str(pancakes(setup))+"\n")
    output.close()
