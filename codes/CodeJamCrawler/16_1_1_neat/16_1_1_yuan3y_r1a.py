def last_word(s):
    appeared=[]
    result=""
    for x in s:
        if len(appeared)>0 and x>=appeared[-1]:
            result=x+result
        else:
            result+=x
        if x not in appeared:
            appeared.extend(x)
            appeared=sorted("".join(list(set(appeared))))
    return result

t = int(input())
for i in range(t):
    s = input()
    lw = last_word(s)
    print("Case #{}: {}".format(i+1,lw))