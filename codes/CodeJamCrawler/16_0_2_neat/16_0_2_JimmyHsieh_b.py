def conv_to_numeric(s):    
    n = []
    for i in range(len(s)):
        if (s[i] == '+'):
            n.append(1)            
        elif (s[i] == '-'): 
            n.append(-1)
        else:
            raise AssertionError("Unexpected value of input[{}]: {}!".format(i, s[i]))
    return n        
        
    
def pickup(s):    
    for i in range(len(s)):
        if (i == 0):
            side = s[i]
        else:
            if (s[i] != side):
                return i    
    return len(s)

def flip(s, num):
    tops = s[:num]
    remains = s[num:]
    tops.reverse()
    tops = [n * (-1) for n in tops]
    tops.extend(remains)    
    return tops
    
    
def solve(stack):
    count = 0
    s = stack
    while(sum(s) != len(s)):
        s = flip(s, pickup(s))
        count = count + 1
    return count
        
    
if __name__ == "__main__":
    t = int(input()) 
    for i in range(1, t + 1):        
        stack = conv_to_numeric(input())        
        print("Case #{}: {}".format(i, solve(stack)))
