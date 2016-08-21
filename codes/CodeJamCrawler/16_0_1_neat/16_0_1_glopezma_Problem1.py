import sys
def check(l): #check if all values are 0
    for i in range(len(l)):
        if not l[i]:
            return False
    return True

def main():
    inputFile = "input.in"
    outputFile = "output.txt"
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w')
    count = int(fin.readline()) #number of values
    check_list = [0]*10
    for i in range(count):
        #reset check back to normal
        for j in range(10):
            check_list[j]=False
        count = 1
        true = False
        num = int(fin.readline()) #number of value
        if(num == 0):
            value = str("Case #"+str(i+1)+": "+"INSOMNIA\n")
            fout.write(value)
        else:
            while(not true):
                ans = str(num*count)
                for ch in ans:
                    check_list[int(ch)] = True
                if check(check_list):
                    value = str("Case #"+str(i+1)+": "+ans+"\n")
                    fout.write(value)
                    true = True
                else:
                    count = count + 1
