import itertools, math

def RevengeofthePancakes(s):
    if ((s=="-") or (s=="-+")):
        return 1
    elif ((s=="+") or (not "-" in s)):
        return 0
    elif (s=="+-"):
        return 2
    else:
        i=0
        s1 = s
        while ( "-" in s):
            #print s,i
            p = s.rfind('-')
            ps = s[:p+1]
            ps = ps.replace('-','.')
            ps = ps.replace('+','-')
            ps = ps.replace('.','+')
            s=ps+s[p+1:]
            #print s, p#, s[:p+1],s[p+1:], ps, ps+s[p+1:]
            i+=1
        return i
        
def MainRevengeofthePancakes():
    print "start"
    in_file = open('C:\\Users\\mkader\\downloads\\B-large.in', 'r')
    ou_file = open('C:\\Users\\mkader\\downloads\\coinjam_out.txt', 'w')

    case = 1;
    in_file.readline();
    for in_data in in_file:
        ldata = in_data.strip(' \t\n\r')
        if(len(ldata)==0):
            break;
        else:
            t = RevengeofthePancakes(ldata)
            #print'Case #'+str(case)+': ' + str(t)
            print>>ou_file,'Case #'+str(case)+': ' + str(t)
        case+=1
    ou_file.close()
    print "done"

MainRevengeofthePancakes()

