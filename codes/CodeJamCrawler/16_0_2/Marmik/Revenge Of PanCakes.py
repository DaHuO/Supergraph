
def solve(string,n,z):
    if len(string) == 1 and string[0] == "+" :
        print("Case #", z+1, ": ",n , sep = '');
        return n;
    if string[len(string)-1] == "+" :
        solve(string[0:len(string)-1],n,z);
    else :
        tempString = [];
        for j in string:
            tempString.append(j);
        for i in range(len(tempString)) :
            if tempString[i] == "+" :
                tempString[i] = "-";
            else :
                tempString[i] = "+";
        string = ''.join(tempString);
        
        solve(string,n+1,z);
		
cases = int(input());

for i in range(cases) :
    string = input();
    if len(string) == 1 :
    	if string[0] == "-" :
    		print("Case #", i+1, ": 1", sep = '');
    	else :
    		print("Case #", i+1, ": 0", sep = '')
    	continue;
    #Check if all values are same
    if string == "-" * len(string) :
    	print("Case #", i+1, ": 1", sep = '');
    	continue;
    elif string == "+" * len(string) :
    	print("Case #", i+1, ": 0", sep = '');
    	continue;
    #Check if all values except last are same
    if string[len(string)-1] == "-" and string[0:len(string)-2] == "+" * (len(string)-2) :
    	print("Case #", i+1, ": 2", sep = '');
    	continue;
    elif string[len(string)-1] == "+" and string[0:len(string)-2] == "-" * (len(string)-2) :
    	print("Case #", i+1, ": 1", sep = '');
    	continue;
    solve(string,0,i);
