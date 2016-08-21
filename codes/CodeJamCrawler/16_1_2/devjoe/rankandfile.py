def printout(casenum,n,position,otherlist,reports):
  nths=[reports[i][position] for i in xrange(len(reports))]
  nths.sort()
  for i in xrange(n):
    if i!=position:
      del nths[nths.index(otherlist[i])]
  print "Case #"+str(j+1)+": "+" ".join(map(str,nths))

t=input()
for j in xrange(t):
  n=input()
  reports=[]
  for k in xrange(2*n-1):
    reports.append(map(int,raw_input().strip().split()))
  reports.sort()
  #n is minimum 2, so there are always at least 3 lists.
  if reports[0][0]!=reports[1][0]:
    #missing the first row or column
    printout(j,n,0,reports[0],reports)
  else:
    nths=[]
    for k in xrange(n):
      nths.append([reports[i][k] for i in xrange(len(reports))])
    #first two reports are the first row and first column in some order.
    #choose arbitrarily.
    frow=reports[0]
    fcol=reports[1]
    positions=[0,0]
    nrow=1
    ncol=1
    nrep=2
    missfirst=max(frow+fcol) #if the last list is missing we won't find it
    #repeatedly try and place the next list.
    while nrep<len(reports):
      if nrow<n and ncol<n and frow[nrow]==fcol[ncol]:
        #next first number appears at the start of a row and a column
        #do I have both of them?
        if nrep<len(reports)-1 and reports[nrep][0]==reports[nrep+1][0]:
          #yes. does it matter where each goes?
          if nrow==ncol:
            #nope
            positions.append(nrow)
            positions.append(ncol)
          else:
            #yes. Use intersection of these rows to determine placements
            nm=min(nrow,ncol)
            if reports[nrep][nm]<reports[nrep+1][nm]:
              if nm==nrow:
                positions.append(nrow)
                positions.append(ncol)
              else:
                positions.append(ncol)
                positions.append(nrow)
            else:
              if nm==ncol:
                positions.append(nrow)
                positions.append(ncol)
              else:
                positions.append(ncol)
                positions.append(nrow)
          nrow+=1
          ncol+=1
          nrep+=2
        else:
          #nope, so we skip the one we have for now and mark it as the missing
          #first number
          missfirst=reports[nrep][0]
          positions.append(-1)
          nrow+=1
          ncol+=1
          nrep+=1
      elif nrow<n and (ncol==n or frow[nrow]<fcol[ncol]):
        #next number needed is for a row.
        if reports[nrep][0]==frow[nrow]:
          #and we have it
          positions.append(nrow)
          nrow+=1
          nrep+=1
        else:
          #it's the missing one
          missfirst=frow[nrow]
          nrow+=1
      else:
        #next number needed is for a column
        if reports[nrep][0]==fcol[ncol]:
          #and we have it
          positions.append(ncol)
          ncol+=1
          nrep+=1
        else:
          #it's the missing one
          missfirst=fcol[ncol]
          ncol+=1
    #now we know where all the lists go except the ones starting with the
    #missing first number.
    if missfirst in frow and missfirst in fcol:
      #missing first number appears as first on another list
      if frow.index(missfirst)==fcol.index(missfirst):
        #in the same position
        otherone=reports[positions.index(-1)]
        printout(j,n,frow.index(missfirst),otherone,reports)
      else:
        #in different positions
        #check whether it works as a row
        trow=frow.index(missfirst)
        tcol=fcol.index(missfirst)
        otherone=reports[positions.index(-1)]
        crosscol=reports[positions.index(trow)]
        combine=otherone+crosscol
        del combine[tcol] #this will be missing at the column if this works
        nths=[reports[i][trow] for i in xrange(len(reports))]
        combine.sort()
        nths.sort()
        if nths==combine:
          printout(j,n,tcol,reports[positions.index(tcol)],reports)
        else:
          printout(j,n,trow,crosscol,reports)
    else:
      #missing first number is unique
      if missfirst in frow:
        position=frow.index(missfirst)
      else:
        position=fcol.index(missfirst)
      otherone=reports[positions.index(position)]
      printout(j,n,position,otherone,reports)
