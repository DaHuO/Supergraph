x = input()
y = 0
arr = ['0',0,'1',0,'2',0,'3',0,'4',0,'5',0,'6',0,'7',0,'8',0,'9',0]
while y!=x:
    z = input()
    a = 0
    while arr[1] != -1:
        a+=1
        for i in str(z*a):
            if i == arr[0]:
                arr[1]+=1
            if i == arr[2]:
                arr[3]+=1
            if i == arr[4]:
                arr[5]+=1
            if i == arr[6]:
                arr[7]+=1
            if i == arr[8]:
                arr[9]+=1
            if i == arr[10]:
                arr[11]+=1
            if i == arr[12]:
                arr[13]+=1
            if i == arr[14]:
                arr[15]+=1
            if i == arr[16]:
                arr[17]+=1
            if i == arr[18]:
                arr[19]+=1
        if z == 0:
            print  'Case #'+str(y+1)+': INSOMNIA'
            break
        if arr[1] > 0 and arr[3] > 0 and arr[5] > 0 and arr[7] > 0 and arr[9] > 0 and arr[11] > 0 and arr[13] > 0 and arr[15] > 0 and arr[17] > 0 and arr[19] > 0:
            print  'Case #'+str(y+1)+': '+ str(z*a) 
            break
    arr = ['0',0,'1',0,'2',0,'3',0,'4',0,'5',0,'6',0,'7',0,'8',0,'9',0]
    y+=1
