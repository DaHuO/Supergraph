in_file = open('A-large.in','r');

out_file = open('A-large-result','w');

cases = int(in_file.readline());

y=[]

for line in range(0, cases):
    number=int(in_file.readline())
    is_here=[0,0,0,0,0,0,0,0,0,0]
    if number==0:
        y+=[-1]
        #print(y)
    else:
        i=0
        while 0 in is_here:
            i+=1
            case=str(number*i)
            #print("case=",case)
            for digit in case:
                #print("digit=",digit)
                this_digit=int(digit)
                is_here[this_digit]=1
                #print(is_here)
        y+=[int(case)]
        #print(case,y)

j=0
for val in y:
    j+=1
    if val==-1:
        out_file.write("Case #")
        out_file.write(str(j))
        out_file.write(": INSOMNIA\n")
    else:
        out_file.write("Case #")
        out_file.write(str(j))
        out_file.write(": ")
        out_file.write(str(val))
        out_file.write("\n")

out_file.close()
