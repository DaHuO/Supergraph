file1 = open(r"C:\Users\Wu Jui Hsuan\Desktop\prob.txt","r")
file = open(r"C:\Users\Wu Jui Hsuan\Desktop\gjmi.txt","w")
def fun(L):
    if L == []:
        return 0
    if L.count("-") == 0:
        return 0
    c = 0
    i = L.index("-")
    if i != 0:
        c = 1
    index = i+1
    while index < len(L) and L[index] == "-":
        index += 1
    return c + 1 + fun(L[index:])
T = int(file1.readline())
for i in range(T):
    s = file1.readline()
    L = [x for x in s]
    r = fun(L)
    print("Case #%d: %d" % (i+1,r))
    file.write("Case #%d: %d\n" % (i+1,r))