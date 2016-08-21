numbers={'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}
number_list=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

String= "ESROUSIXENVF"

def find_number(String):
    new_string=String
    if len(String)==0:
        return []
    poss_number=[]
    for number in number_list:
        i=0
        temp_string=String
        for number_letter in number:
            found=False
            for string_letter in temp_string:
                if number_letter==string_letter:
                    i=i+1
                    found=True
                    temp_string=temp_string.replace(number_letter,'',1)
                    break
            if not found:
                break
        
        if i==len(number):
            found=True
            #FOUND!
            poss_number.append(number)
    for number in poss_number:
        new_string=String
        for number_letter in number:
            new_string=new_string.replace(number_letter,'',1)
        
        a=find_number(new_string)
        if a != -1:
            return [numbers[number]]+a
    return -1
StringArray=[]


cases=input("Test Cases:")
number=int(cases)
for i in range(0,number):
    StringArray.append(input("String:"))
    
i=1 
for String in StringArray:
    array=find_number(String)
    out="Case #"+str(i)+": "
    for number in array:
        out=out+str(number)
    print(out)
    i=i+1
        
