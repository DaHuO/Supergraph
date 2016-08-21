import io
file = io.open('./B-large.in.txt','r')
i = 0
def solver(input):
    input = input.strip()
    if len(input.rstrip("+"))==0:
        return(0)
    else:
        if input[-1] == '-':
            inp = ""
            for char in input:
                if char == "+":
                    inp += "-"
                else:
                    inp += "+"
            if inp[0] == '-':
                input2 = input.rstrip('-')
                inp2 = ''
                for char in input2:
                    if char == "+":
                        inp2 += "-"
                    else:
                        inp2 += "+"
                return(1+solver(inp2[::-1]+input[len(inp2):]))

            else:
                return(1+solver(inp[::-1]))
        else:
            return(solver(input.rstrip("+")))

for line in file:
    if i == 0:
        i += 1
        next
    else:
        print("Case #" + str(i)+ ": " + str(solver(line)))
        i+=1

