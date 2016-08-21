def get_lifts(s):
    end = s.rfind('-')    
    if end == -1:
        return 0

    c = s[0]
    num = 0 
    for i in range(1, end + 1):
        if s[i] != c:
            num += 1
            c = s[i]         
      
    return num + 1

T = int(input())

for i in range(T):
    s = input()
    print('Case #' + str(i + 1) + ': ' + str(get_lifts(s)))

