'''
@author: Christoph Kreutzer
'''

def hasAbsMaj(l):
    total = sum(l)
    for party in l:
        if party > total/2:
            return True
    return False

def evac(members):
    for f in range(len(members)):
        for g in range(len(members)):
            if members[f] < 1 or members[g] < 1:
                continue
            if f == g and members[f] < 2:
                continue
            members[f] -= 1
            members[g] -= 1
            if not hasAbsMaj(members):
                return chr(65+f) + chr(65+g)
            members[f] += 1
            members[g] += 1
        if members[f] < 1:
            continue
        members[f] -= 1
        if not hasAbsMaj(members):
            return chr(65+f)
        members[f] +=1

def main():
    T = int(raw_input())
    for i in range(T):
        n = int(raw_input())
        members = [int(x) for x in raw_input().split()]
        out = ""
        # ord A 65
        while sum(members) > 0:
            out += evac(members) + " "
        print "Case #" + str(i+1) + ": " + str(out[:-1])
        
if __name__ == "__main__":
    main()