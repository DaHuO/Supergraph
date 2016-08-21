rt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(int(input())):
    s = input()
    a = {}
    for k in rt:
        a[k] = 0
    for k in s:
        a[k]+=1
    ans0 = ""
    ans2 = ""
    ans1 = ""
    ans3 = ""
    ans4 = ""
    ans5 = ""
    ans6 = ""
    ans7 = ""
    ans8 = ""
    ans9 = ""
    
    if(a['Z']!=0):
        t = a['Z']
        a['Z'] -= t
        a['E'] -= t
        a['R'] -= t
        a['O'] -= t
        ans0 = "0"*t
    if(a['W']!=0):
        t = a['W']
        a['W'] -= t
        a['O'] -= t
        a['T'] -= t
        ans2 = "2"*t
    if(a['U']!=0):
        t = a['U']
        a['U'] -= t
        a['F'] -= t
        a['O'] -= t
        a['R'] -= t
        ans4 = "4"*t
    if(a['X']!=0):
        t  = a['X']
        a['X'] -= t
        a['I'] -= t
        a['S'] -= t
        ans6 = "6"*t
    if(a['G']!=0):
        t  = a['G']
        a['G'] -= t
        a['E'] -= t
        a['I'] -= t
        a['H'] -= t
        a['T'] -= t
        ans8 = "8"*t
    if(a['O']!=0):
        t  = a['O']
        a['O'] -= t
        a['N'] -= t
        a['E'] -= t
        
        ans1 = "1"*t
    if(a['R']!=0):
        t  = a['R']
        a['R'] -= t
        a['T'] -= t
        a['H'] -= t
        a['E'] -= t
        a['E'] -= t
        
        ans3 = "3"*t
    if(a['F']!=0):
        t  = a['F']
        a['F'] -= t
        a['I'] -= t
        a['V'] -= t
        a['E'] -= t
        
        
        ans5 = "5"*t
    if(a['V']!=0):
        t  = a['V']
        a['V'] -= t
        a['S'] -= t
        a['E'] -= t
        a['N'] -= t
        a['E'] -= t
        
        ans7 = "7"*t
    if(a['I']!=0):
        t  = a['I']
        a['N'] -= t
        a['I'] -= t
        a['N'] -= t
        a['E'] -= t
        
        
        ans9 = "9"*t
    finalans = "Case #" + str(i+1) +": "+ ans0 + ans1 +ans2 +ans3 +ans4 +ans5 +ans6 +ans7 + ans8 +ans9
    print(finalans)
        
        
        
        
        
