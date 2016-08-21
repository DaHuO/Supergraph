with open("Downloads/A.in") as f:
    content = f.readlines()

fo = open("out.txt", "wb")
T=int(content[0])
for case in range(1,T+1):
    room = map(int, content[2*case][:-1].split(' '))
    fo.write("Case #" + str(case) + ": ")
    while sum(room)>0:
        party = room.index(max(room))
        fo.write(chr(ord('A')+party))
        room[party]-=1
        if sum(room)>1 and max(room)*2<=sum(room):
            fo.write(" ")
        if sum(room) == 0:
            fo.write("\n")
fo.close()
print "end"
