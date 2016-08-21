'''
Created on Apr 9, 2016

@author: christoph
'''
def main():
    T = int(raw_input())
    for i in range(T):
        line = raw_input().split()
        k = int(line[0])
        c = int(line[1])
        s = int(line[2])        
        out = [str(x+1) for x in range(s)]
        print "Case #" + str(i+1) + ": " + " ".join(out)
        
if __name__ == '__main__':
    main()