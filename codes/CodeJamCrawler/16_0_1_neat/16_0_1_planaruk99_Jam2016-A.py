
   
#'''
def amount_people(PP) :
  result = 0
  cResult = 0
  PPR = PP[::-1]
  PPR = list(map(int,PPR))
  #printDebug("PPR : ",PPR)
  M2 = len(PP) - 1
  #printDebug("M2 : ",M2)
  for i in range (len(PP)-1) :
    #PPR[i]
    #printDebug("len of less lev",len(PPR[i+1::]))
    lev = len(PPR[i+1::])
    SPPI = sum(PPR[i+1::])
    carry = SPPI-lev
    #if i > 0 :
    if carry > 0 and i == 0:
    #no need
      carry = 0
    elif carry <= 0 and i == 0:
      result = abs(carry)
      
    if i > 0 and carry < 0 and abs(carry) > result  :
      result = abs(carry)
  return result

def formatValue(Ns) :
  Nchar = list(map(int,list(Ns[0])))
  #Nchar = map(chr,list(Ns[0]))
  intNchar = list(map(int,Nchar))
  N = int(Ns[0])  
  return Nchar, N#, intNchar

Padd = 0
countLine=0
countCase = 1 
result = 0
#example.in
#D-small-practice.in
#'A-EX.in'
#'A-small-attempt0.in'
with open('A-large.in','r') as ifile, open('outputJam2016-A-large.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
  for line in ifile :
    #print (line)
    print("6666666666666666666666666666666666666666666666666")
    if countLine == 0 :
      case = line.split()
      case = int(case[0])
      print ("case : ",case)
      #case = int(line.split())
    elif countLine >= 1 and countCase >= 0 and countCase <= case :
      Ns = line.split()
      #Nchar = map(int,list(Ns[0]))
      #Nchar=line.strip()
      #wList[:0] = w          
      #intNchar = map(int,Nchar)
      #N = int(Ns[0])
  
      Nchar, N = formatValue(Ns)
      #,' intNchar : ',intNchar
      print(" Ns : ",Ns," N : ",N,' Nchar : ',Nchar)
      #,' ns[3][1] : ',Ns[2][1]
      if N == 0 :
        result = 'INSOMNIA'
      else :
        #print(len(set(Nchar)))
        NcharAll = Nchar[:]
        '''
        print("NcharAll : ",NcharAll,len(set(NcharAll)))
        #NcharAll.extend(['2','3'])
        #print("NcharAll : ",NcharAll)  
        N=N*2
        print("N : ",N)
        N = str(N)
        print("N : ",N)
        Ns = N.split()
        print("Ns : ",Ns)
        Nchar, N = formatValue(Ns)
        print("Nchar : ",Nchar)
        NcharAll.extend(Nchar)
        print("NcharAll : ",NcharAll)  
        
        '''
        i=2
        while len(set(NcharAll))<10 :
          #print("set(NcharAll) : ",set(NcharAll))
          newN=N*i
          i=i+1
          #print("newN : ",newN)
          newN = str(newN)
          #print("N : ",N)
          Ns = newN.split()
          #print("Ns : ",Ns)
          Nchar, newN = formatValue(Ns)
          print("newN : ",newN)
          #print("Nchar : ",Nchar)
          NcharAll.extend(Nchar)
          #print("NcharAll : ",NcharAll)
          print("set(NcharAll) : ",set(NcharAll))
          #print("solution : ",newN)
        
        #print("test")
        result = newN
        
      #if 
      '''
      [M, PP] = map(str, line.split())
      M = int(M)
      PP = str(PP)
      PP = iter(PP)
      PP = ' '.join(PP)
      PP = PP.split()
      result = amount_people(PP)
      '''
      
      
      outLine = 'Case #'+str(countCase)+': '+str(result)+'\n'
      print(outLine)
      ofile.write(outLine)
      countCase = countCase + 1
    else :
      printDebug("IMPORSIBLE ??!!",99)
    if countCase > case : 
      #print("break")
      break
    countLine = countLine + 1

ifile.close()
ofile.close()
oDfile.close()
oRfile.close()


