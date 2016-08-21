f = open("A-large.in", 'r')
fo = open("A-large.out", 'w')

t = int(f.readline())

init_arr = [0,1,2,3,4,5,6,7,8,9]

def reset():
    global init_arr
    init_arr = [0,1,2,3,4,5,6,7,8,9]
def check(arr):
    for s in arr:
        try:
            init_arr.pop(init_arr.index(int(s)))
        except:
            pass
    if len(init_arr) == 0:
        return False
    return True

for i in range(t):
    reset()
    n = int(f.readline())
    passed = False
    if n == 0:
        fo.write("Case #"+str(i+1)+": INSOMNIA\n")
        continue
    for z in range(1,100):
        if not check(str(z*n)):
            fo.write("Case #"+str(i+1)+": "+str(z*n)+"\n")
            passed = True
            break
    if not passed:
        fo.write("Case #"+str(i+1)+": INSOMNIA\n")