def helper(x: int):
    temp = []
    count = 2
    current = x
    if x==0:
        return "Insomnia"
    else:
        for i in str(current):
            if i not in temp:
                temp.append(i)
        while 1:
            if len(temp) != 10:
                current= x*count
                for i in str(current):
                    if i not in temp:
                        temp.append(i)
                count+=1
            else:
                break       
    return current

if __name__ == '__main__':
    file = open('A-large.in')
    user_input = file.readlines()
    for i in range(len(user_input)):
        user_input[i]= user_input[i].strip()
    for i in range(1,len(user_input)):
        print("Case #"+str(i)+": "+str(helper(int(user_input[i]))))
        
    
    
