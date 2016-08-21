import math
import random
import itertools
from decimal import *
import cProfile
import scipy.optimize
from scipy.optimize import linprog



class arc:
  def __init__(self, source, sink, rev, cap):
    self.source = source
    self.sink = sink
    self.rev = rev
    self.flow = 0
    self.cap = cap

# Source: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
class FlowNetwork(object):
  def __init__(self):
    self.vert = {}
    self.vertName = []
    self.vertCntr = 0
    self.G = []
 
  def add_vertex(self, vertex):
    assert(vertex not in self.vert)
    self.vertName.append(vertex)
    self.vert[vertex] = self.vertCntr
    self.vertCntr = self.vertCntr + 1
    self.G.append([])

  def get_edges(self, v):
    if(type(v) is str):
      v = self.vert[v]
    return self.G[v]
 
  # Add to G a directed arc (u,v) of capacity cap
  # and a reverse arc (v,u) of capacity rcap
  def add_edge(self, u, v, w, rcap=0):
    if u == v:
      raise ValueError("u == v")
    if(type(u) is str):
      u = self.vert[u]
      v = self.vert[v]
    uv_pos = len(self.G[u])
    vu_pos = len(self.G[v])
    self.G[u].append( arc(u,v,vu_pos,w))

    # reverse arc
    self.G[v].append( arc(v,u,uv_pos,rcap))

  # Try pushing f units of flow from u to t via a DFS
  # Use the BFS distance labels dist[]
  # and the DFS "next arc" counters work[]
  # Return the amount of routable flow and update the residual graph and arc counters
  def dinic_dfs(self, u, t, f, dist, work): 
    if u == t: return f
    deg_u = len(self.G[u])
    w_u = work[u]
    for i in range(w_u, deg_u): # ***
      e = self.G[u][i]
      work[u] = i
      v = e.sink 
      if e.flow < e.cap and dist[v] == dist[u] + 1:
        df = self.dinic_dfs(v, t, min(f, e.cap - e.flow), dist, work)
        if df > 0:
          e.flow += df
          self.G[e.sink][e.rev].flow -= df
          return df
    return 0

  # Compute distance labels of a BFS rooted at s, store them in dist[0..n-1]
  # Return (reach, dist), where
  # reach is true iff t is reachable from s in the residual graph
  def dinic_bfs(self, s, t):
    dist = [None]*len(self.G)
    q = [s]
    dist[s] = 0
    while len(q) > 0:
      u = q.pop(0)
      for e in self.G[u]:
        v = e.sink
        if e.cap - e.flow > 0 and dist[v]==None:
          dist[v] = dist[u] + 1
          q.append(v)
    return (dist[t] != None, dist)

  # Return the maximum value of an s-t flow in n-node graph G
  def max_flow(self, source, sink):
    if(type(source) is str):
      source = self.vert[source]
      sink = self.vert[sink]

    INF = float('inf')
    mf = 0
    while True:
      [reach, dist] = self.dinic_bfs(source, sink)
      if not reach: break
      work = [0]*len(self.G) # reset DFS
      while True:
        df = self.dinic_dfs(source, sink, INF, dist, work)
        mf += df
        if df == 0: break
    return mf

getcontext().prec = 100
#openfile = open("test.t", 'r')
openfile = open("A-large.in", 'r')
#openfile = open("C-large-practice.in", 'r')
d = openfile.read().splitlines()
n = int(d[0])


def addNew(cc, seq):
  sum = 0
  for _ in range(len(cc)):
    sum = sum  + cc[_]
  if(max(cc)*2 > sum):
    return []

  ccX = [_ for _ in cc]
  seqX = [_ for _ in seq]
  m = 0
  mId = -1
  for _ in range(len(ccX)):
    if(m < ccX[_]):
      m = ccX[_]
      mId = _
  if(m == 0):
    return seqX

  ccX[mId] = ccX[mId] - 1
  seqX.append(chr(mId+65))

  m = 0
  mId = -1
  for _ in range(len(ccX)):
    if(m < ccX[_]):
      m = ccX[_]
      mId = _
  if(m == 0):
    return seqX
  ccX[mId] = ccX[mId] - 1
  seqX[-1] = seqX[-1] + chr(mId+65)

  dd = addNew(ccX, seqX)
  
  if(len(dd) == 0):
    ccX = [_ for _ in cc]
    seqX = [_ for _ in seq]
    m = 0
    mId = -1
    for _ in range(len(ccX)):
      if(m < ccX[_]):
        m = ccX[_]
        mId = _
    if(m == 0):
      return seqX

    ccX[mId] = ccX[mId] - 1
    seqX.append(chr(mId+65))
    return addNew(ccX, seqX)
  else:
    return dd


linId = 1
for tcNum in range(0,n):
  cc = d[linId].split()
  linId = linId + 1
  cc = [int(_) for _ in d[linId].split()]
  linId = linId + 1

  seq = []
  seq = addNew(cc, seq)

  print 'Case #' + str(tcNum+1) + ": " + ' '.join(seq)
  
if(0):
  linId = 1
  for tcNum in range(0,n):
    cc = d[linId].split()
    linId = linId + 1
    numSources = int(cc[0])
    vTot = float(cc[1])
    xTot = float(cc[2])
    
    v = []
    x = []
    A_eq = [[],[]]
    nn = 0
    rr = 0
    for _ in range(numSources):
      cc = d[linId].split()
      linId = linId + 1
      if(float(cc[1]) != xTot):
        v.append(float(cc[0]))
        x.append(float(cc[1]))
        nn = nn + 1

        A_eq[0].append(1)
        A_eq[1].append(x[-1])
      else:
        rr = rr + float(cc[0])

    A_eq[0].append(0)
    A_eq[1].append(0)
    b_eq = [1,xTot]
    
    A_ub = []
    b_ub = []

    for _ in range(nn):
      u = [0 for __ in range(nn+1)]
      u[_] = 1
      u[-1] = -v[_]
      A_ub.append(u)
      b_ub.append(0)

    c = [0 for __ in range(nn+1)]
    c[-1] = 1

    ret = 'IMPOSSIBLE'
    if(len(v) > 1):
      res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,options={'bland': False, 'tol': 1e-12, 'maxiter': 10000})
      if(res.status == 0):
        ret = str(res.x[-1])
        ret = '{0:.10f}'.format(res.x[-1] * vTot)
    elif(rr > 0):
      ret = '{0:.10f}'.format(vTot / rr)
    if(0):
      if(tcNum+1 == 39):
        print c
        print A_ub
        print b_ub
        print A_eq
        print b_eq
        print v,x
        print vTot,xTot
        print '-----'
        print A_ub, b_ub
        print A_eq, b_eq
        print res
        print nn, rr
        print ret
        assert(0)
    print 'Case #' + str(tcNum+1) + ": " + ret


if(0):
  #https://code.google.com/codejam/contest/8234486/dashboard#s=p2&a=3
  #https://www.topcoder.com/community/data-science/data-science-tutorials/maximum-flow-section-1/
  #https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-graphs-and-their-data-structures-section-1/
  linId = 1
  inf = 1000000
  for tcNum in range(0,n):
    g = FlowNetwork()
    g.add_vertex('startXAMS')
    g.add_vertex('endXAMS')

    s = int(d[linId])
    linId = linId + 1
    words = {}
    for jfk in range(s):
      sentId = 'Sentence' + str(jfk)
      g.add_vertex(sentId)
      sent = [_ for _ in set(d[linId].split())]
      linId = linId + 1
      for w in range(len(sent)):
        if(sent[w] not in words):
          words[sent[w]] = []
          g.add_vertex(sent[w]+'English')
          g.add_vertex(sent[w]+'Frensh')
        words[sent[w]].append(sentId)

    cntr = 0
    for w in words:
      if(len(words[w]) > 1):
        g.add_edge('startXAMS', w+'English',1)
        g.add_edge(w+'Frensh', 'endXAMS',1)
        cntr = cntr + 1

        for sentId in words[w]:
          g.add_edge(w+'English', sentId ,inf)
          g.add_edge(sentId, w+'Frensh' ,inf)

    g.add_edge('startXAMS', 'Sentence' + str(0),inf)
    g.add_edge('Sentence' + str(1), 'endXAMS',inf)
    #cProfile.run('g.max_flow(\'startXAMS\',\'endXAMS\') - cntr')
    print 'Case #' + str(tcNum+1) + ": " + str(g.max_flow('startXAMS','endXAMS') - cntr)

    #for _ in g.get_edges('startXAMS'):
    #  print g.vertName[_.source], g.vertName[_.sink], _.flow

if(0):
  linId = 1
  for tcNum in range(0,n):
    s = int(d[linId])
    linId = linId + 1
    li = []
    fir = []
    sec = []
    for i in range(s):
      li.append(d[linId].split())
      fir.append(li[-1][0])
      sec.append(li[-1][1])
      linId = linId + 1
    g = FlowNetwork()
    g.add_vertex('startXAMS')
    g.add_vertex('endXAMS')
    for a in set(fir):
      g.add_vertex(a+'XAMS0')
      g.add_edge('startXAMS', a+'XAMS0',1)
    for a in set(sec):
      g.add_vertex(a+'XAMS1')
      g.add_edge(a+'XAMS1', 'endXAMS',1)
    for a in li:
      g.add_edge(a[0] + 'XAMS0', a[1] + 'XAMS1',1)

    orig = g.max_flow('startXAMS','endXAMS')
    for _ in g.get_edges('startXAMS'):
      if(_.flow == 0):
        orig = orig + 1

    for a in set(sec):
      f = 0
      for _ in g.get_edges(a+'XAMS1'):
        if((_.sink == g.vert['endXAMS']) and (_.flow == 0)):
          f = 1
          break
      if(f == 1):
        orig = orig + 1
    print 'Case #' + str(tcNum+1) + ": " + str(s-orig)

if(0):
  def selPattern(s0, s1):
    if(len(s0) == 0):
      return s1
    if(len(s1) == 0):
      return s0
    s0x = [[],[]]
    s1x = [[],[]]
    s0x[0] = int(''.join(s0[0]))
    s0x[1] = int(''.join(s0[1]))
    s1x[0] = int(''.join(s1[0]))
    s1x[1] = int(''.join(s1[1]))
    if(abs(s0x[0] - s0x[1]) < abs(s1x[0] - s1x[1])):
      return s0
    if(abs(s0x[0] - s0x[1]) > abs(s1x[0] - s1x[1])):
      return s1
    if(abs(s0x[0]) < abs(s1x[0])):
      return s0
    if(abs(s0x[0]) > abs(s1x[0])):
      return s1
    if(abs(s0x[1]) < abs(s1x[1])):
      return s0
    if(abs(s0x[1]) > abs(s1x[1])):
      return s1
    return s0

  def changeX(s):
    gr = -1
    for i in range(len(s[0])):
      if(s[0][i] == '?' or s[1][i] == '?'):
        break
      if(int(s[0][i]) > int(s[1][i])):
        gr = 0
        break
      if(int(s[0][i]) < int(s[1][i])):
        gr = 1
        break
    f = 0
    for i in range(len(s[0])):
      if(s[0][i] == '?' or s[1][i] == '?'):
        f = 1
        break
    if(f == 0):
      return s

    ss0 = []
    if(gr == -1):
      if(s[0][i] == '?' and s[1][i] == '?'):
        ra = '01'
        if(i < len(s[0])-1 and (s[0][i+1] == '?') and (s[1][i+1] == '?')):
          ra = '0'
        for kl in ra:
          for lk in ra:
            ss = [[],[]]
            ss[0] = [_ for _ in s[0]]
            ss[1] = [_ for _ in s[1]]
            ss[0][i] = kl
            ss[1][i] = lk
            ss0 = selPattern(ss0, changeX(ss))
      elif(s[0][i] == '?'):
        ss = [[],[]]
        ss[0] = [_ for _ in s[0]]
        ss[1] = [_ for _ in s[1]]
        ss[0][i] = s[1][i]
        ss0 = selPattern(ss0, changeX(ss))
        if(int(s[1][i]) < 9):
          ss = [[],[]]
          ss[0] = [_ for _ in s[0]]
          ss[1] = [_ for _ in s[1]]
          ss[0][i] = str(int(s[1][i]) + 1)
          ss0 = selPattern(ss0, changeX(ss))
        if(int(s[1][i]) > 0):
          ss = [[],[]]
          ss[0] = [_ for _ in s[0]]
          ss[1] = [_ for _ in s[1]]
          ss[0][i] = str(int(s[1][i]) - 1)
          ss0 = selPattern(ss0, changeX(ss))
      elif(s[1][i] == '?'):
        ss = [[],[]]
        ss[0] = [_ for _ in s[0]]
        ss[1] = [_ for _ in s[1]]
        ss[1][i] = s[0][i]
        ss0 = selPattern(ss0, changeX(ss))
        if(int(s[0][i]) < 9):
          ss = [[],[]]
          ss[0] = [_ for _ in s[0]]
          ss[1] = [_ for _ in s[1]]
          ss[1][i] = str(int(s[0][i]) + 1)
          ss0 = selPattern(ss0, changeX(ss))
        if(int(s[0][i]) > 0):
          ss = [[],[]]
          ss[0] = [_ for _ in s[0]]
          ss[1] = [_ for _ in s[1]]
          ss[1][i] = str(int(s[0][i]) - 1)
          ss0 = selPattern(ss0, changeX(ss))
      return ss0
    elif(gr == 0):
      for _ in range(i, len(s[0])):
        if(s[0][_] == '?'):
          s[0][_] = '0'
        if(s[1][_] == '?'):
          s[1][_] = '9'
    elif(gr == 1):
      for _ in range(i, len(s[0])):
        if(s[0][_] == '?'):
          s[0][_] = '9'
        if(s[1][_] == '?'):
          s[1][_] = '0'
    return s

  for tcNum in range(0,n):
    s = d[tcNum+1].split()
    s[0] = [_ for _ in s[0]]
    s[1] = [_ for _ in s[1]]
    s = changeX(s)
    print 'Case #' + str(tcNum+1) + ": " + ''.join(s[0]) + ' ' + ''.join(s[1])#, '>>>>', d[tcNum+1]
    

if(0):
  for tcNum in range(0,n):
    s = d[tcNum+1]
    s0 = s
    xx = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    ll = []
    indicesX = [0, 6, 2, 7, 8, 3, 4, 1, 5, 9]
    for i in range(len(xx)):
      while(1):
        ss = s
        for _ in xx[indicesX[i]]:
          f = ss.find(_)
          if(f == -1):
            break
          ss = ss[:f] + ss[f+1:]
        if(f != -1):
          s = ss
          ll.append(indicesX[i])
        else:
          break
    if(len(s) != 0):
      print s0
      print s
      assert(0)
    ll.sort()
    ll = [str(_) for _ in ll]
    print 'Case #' + str(tcNum+1) + ": " + ''.join(ll)
  
if(0):
  def addSt(bbf,cc,s):
    cir = [cc]
    cdc = cir[-1]
    start = len(cir)
    typClose = -1
    while(1):
      nxt = bbf[cir[-1]]
      if((len(cir) > 1) and (nxt == cir[-2])):
        typClose = 0
        break
      elif(nxt in cir):
        if(nxt == cir[0]):
          typClose = 1
        else:
          typClose = -1
        break
      else:
        cir.append(nxt)
    return [cir, typClose]

  linId = 1
  for tcNum in range(0,n):
    s = int(d[linId])
    linId = linId + 1
    bbf = [int(_)-1 for _ in d[linId].split()]
    linId = linId + 1

    ll = -1
    endMax = [[] for _ in range(s)]
    for st in range(s):
      lk = addSt(bbf,st,s)
      if(lk[1] == 1):
        ll = max(ll, len(lk[0]))
      elif(lk[1] == 0):
        if(len(endMax[lk[0][-1]]) < len(lk[0])):
          endMax[lk[0][-1]] = lk[0]

    tot = 0
    for _ in endMax:
      if(len(_) > 0):
        tot = tot + len(_) - 1
    ll = max(ll, tot)

    print 'Case #' + str(tcNum+1) + ": " + str(ll)
  

if(0):
  linId = 1
  for tcNum in range(0,n):
    s = int(d[linId])
    linId = linId + 1
    li = []
    for i in range(2*s-1):
      li.append([int(_) for _ in d[linId].split()])
      linId = linId + 1

    ll = []
    for _ in li:
      for __ in _:
        ll.append(__)
    nn = set(ll)
    
    pos = []
    for _ in nn:
      cntr = 0
      for __ in ll:
        if(_ == __):
          cntr = cntr + 1
      if(cntr%2 == 1):
        pos.append(_)  
    
    if(0):
      c = []
      for i in range(s):
        k = [_[i] for _ in li]
        for _ in pos:
          cntr = 0
          for __ in k:
            if(__ == _):
              cntr = cntr + 1
          if(cntr%2 == 1):
            c.append(str(_))
      if(len(c) != s):
        print linId
        print tcNum
        print c
        print pos
    else:
      pos.sort()
      c = [str(_) for _ in pos]
    
    assert(len(c) == s)
    print 'Case #' + str(tcNum+1) + ": " + ' '.join(c)


if(0):
  linId = 1
  for tcNum in range(0,n):
    s = [ord(_) for _ in d[linId]]
    linId = linId + 1

    ss = [s[0]]
    s = s[1:]
    
    while(len(s) > 0):
      if(s[0] >= ss[0]):
        sss = [s[0]]
        for _ in ss:
          sss.append(_)
        ss = sss
      else:
        ss.append(s[0])
      s = s[1:]

    st = ''
    for _ in ss:
      st = st + chr(_)
    print 'Case #' + str(tcNum+1) + ": " + st


if(0):
  cc = [['<', 0, -1], ['>', 0, 1], ['^', -1, 0], ['v', 1, 0]]

  linId = 1
  for tcNum in range(0,n):
    n = d[linId].split()
    r = int(n[0])
    c = int(n[1])
    linId = linId + 1
    aa = []
    arrows = []
    er = 0
    for i in range(r):
      aa.append(d[linId])
      for _ in cc:
        ind = -1
        while(1):
          ind = d[linId].find(_[0], ind + 1)
          if(ind == -1):
            break
          arrows.append([d[linId][ind], i, ind])
      linId = linId + 1
      
    changes = 0
    for k in arrows:
      pos = [k[1], k[2]]
      for _ in cc:
        if(_[0] == k[0]):
          ch = _[1:]
      er = 0
      while(1):
        pos[0] = pos[0] + ch[0]
        pos[1] = pos[1] + ch[1]
        if((pos[0] < 0) | (pos[1] < 0) | (pos[0] > r-1) | (pos[1] > c-1)):
          er = 1
          break
        if(aa[pos[0]][pos[1]] != '.'):
          break
      if(er == 1):
        changes = changes + 1
        for xx in cc:
          pos = [k[1], k[2]]
          ch = xx[1:]
          while(1):
            pos[0] = pos[0] + ch[0]
            pos[1] = pos[1] + ch[1]
            if((pos[0] < 0) | (pos[1] < 0) | (pos[0] > r-1) | (pos[1] > c-1)):
              break
            if(aa[pos[0]][pos[1]] != '.'):
              er = 0
              break
      if(er == 1):
        break
    if(er == 1):
      print 'Case #' + str(tcNum+1) + ": " + "IMPOSSIBLE"
    else:
      print 'Case #' + str(tcNum+1) + ": " + str(changes)

if(0):
  linId = 1
  for tcNum in range(0,n):
    n = int(d[linId])
    linId = linId + 1
    m = int(d[linId])
    linId = linId + 1
    mmm = []
    for _ in range(m):
      x = d[linId].split()
      linId = linId + 1
      mm = []
      for i in range(1,len(x),2):
        mm.append([int(x[i])-1, int(x[i+1])])
      mmm.append(mm)

    sel = [0 for _ in range(n)]
    while(1):
      ff = 0
      for i in range(m):
        sat = 0
        where1 = -1
        where0 = -1
        for _ in mmm[i]:
          if(_[1] == sel[_[0]]):
            sat = 1
          if(_[1] == 1):
            where1 = _[0]
          if(_[1] == 0):
            where0 = _[0]
        if(sat == 0):
          if(where1 >= 0):
            sel[where1] = 1
            ff = 1
            break
          if(where0 >= 0):
            ff = -1
            break
      if(ff <= 0):
        break
    if(ff == -1):
      print 'Case #' + str(tcNum+1) + ": " + "IMPOSSIBLE"
    else:
      sel = [str(_) for _ in sel]
      print 'Case #' + str(tcNum+1) + ": " + ' '.join(sel)
          

if(0):
  vv = Decimal(3)+Decimal(5).sqrt()
  for tcNum in range(0,n):
    a = int(d[tcNum+1])
    ll = vv ** Decimal(a)
    prod = str(int(ll) % 1000)
    while(len(prod) != 3):
      prod = '0' + prod
    print 'Case #' + str(tcNum+1) + ": " + prod
  

if(0):
  linId = 1
  for tcNum in range(0,n):
    a = int(d[linId])
    linId = linId + 1
    m = []
    for i in range(a):
      m.append([int(_) for _ in d[linId].split()])
      linId = linId + 1

    intersects = 0
    for i1 in range(a):
      for i2 in range(i1+1, a):
        diff = [m[i1][0] - m[i2][0], m[i1][1] - m[i2][1]]
        if(not(((diff[0] > 0) & (diff[1] > 0)) | ((diff[0] < 0) & (diff[1] < 0)))):
          intersects = intersects + 1
    print 'Case #' + str(tcNum+1) + ": " + str(intersects)

if(0):
  # King
  linId = 1
  for tcNum in range(0,n):
    a =d[linId].split()
    r = int(a[0])
    c = int(a[1])
    mm = []
    for _ in range(r):
      linId = linId + 1
      mm.append([ii for ii in d[linId]])
      if('K' in d[linId]):
        curr = [_, d[linId].find('K')]
    linId = linId + 1

    changes = [[1,1], [-1,-1], [1,0], [0,1], [1,-1], [-1,1], [-1,0], [0,-1]]
    n = 0
    while(1):
      n = n + 1
      f = 0
      for _ in changes:
        currX = [_[0]+curr[0], _[1]+curr[1]]
        if((currX[0] >= 0) & (currX[1] >= 0) & (currX[0] < r) & (currX[1] < c)):
          if(mm[currX[0]][currX[1]] == '.'):
            f = 1
            mm[currX[0]][currX[1]] = 'K'
            mm[curr[0]][curr[1]] = '#'
            curr = currX
            break
      if(f == 0):
        break
    if(n%2 == 0):
      win = 'B'
    else:
      win = 'A'
    print 'Case #' + str(tcNum+1) + ": " + win
    
    

if(0):
  for tcNum in range(0,n):
    needed = []
    nn = d[tcNum+1].split()
    k = int(nn[0])
    c = int(nn[1])
    s = int(nn[2])
    
    m = [_ for _ in range(k)]
    while(1):
      mm = 0
      for _ in range(c):
        mm = mm + m.pop() * (k**_)
        if(len(m) == 0):
          break
      needed.append(mm+1)
      if(len(m) == 0):
        break
    needed.sort()
    needed = [str(_) for _ in needed]
    if(len(needed) > s):
      needed = ['IMPOSSIBLE']
    print 'Case #' + str(tcNum+1) + ": " + ' '.join(needed)

if(0):
  nBits = 32
  numCoins = 500

  primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  dic = []
  for b in range(2,11):
    dic.append([])
    for p in primes:
      dic[b-2].append([int((b**_)%p) for _ in range(nBits)])
    
  curr = [False for _ in range(nBits)]
  curr[0] = True
  curr[-1] = True

  print 'Case #1:'

  cntr = 0
  while(1):
    fp = []
    for b in range(2,11):
      f = 0
      for c in range(len(primes)):
        rem = 0
        for _ in range(nBits):
          if(curr[_] == True):
            rem = rem + dic[b-2][c][_]
        rem = rem % primes[c]
        if(rem == 0):
          f = 1
          fp.append(str(primes[c]))
          break
      if(f == 0):
        break
    if(f == 1):
      mc = ''
      for _ in range(nBits):
        if(curr[-1-_]==True):
          mc = mc + '1'
        elif(curr[-1-_]==False):
          mc = mc + '0'
      print mc + ' ' + ' '.join(fp)
      cntr = cntr + 1
      if(cntr == numCoins):
        break
    f = 0
    for _ in range(1,nBits-1):
      curr[_] = not(curr[_])
      if(curr[_] == True):
        f = 1
        break
    assert(f == 1)


if(0):
  for tcNum in range(0,n):
    c = d[tcNum+1]
    a = []
    for _ in c:
      if(_ == '+'):
        a.append(True)
      else:
        a.append(False)

    steps = 0
    while(1):
      f = 1
      for _ in a:
        if(_ == False):
          f = 0
          break
      if(f == 1):
        break

      steps = steps + 1
      a[0] = not(a[0])
      for _ in range(1,len(a)):
        if(a[_] != a[0]):
          a[_] = not(a[_])
        else:
          break
    print 'Case #' + str(tcNum+1) + ": " + str(steps)

if(0):
  for tcNum in range(0,n):
    c = int(d[tcNum+1])
    x = c
    cntr = 1
    st = [0 for _ in range(10)]
    if(c != 0):
      while(1):
        x = c * cntr
        for _ in str(x):
          st[int(_)] = 1
        f = 1
        for _ in range(10):
          if(st[_] == 0):
            f = 0
            break
        if(f == 1):
          break
        cntr = cntr + 1
    if(x == 0):
      print 'Case #' + str(tcNum+1) + ": INSOMNIA"
    else:
      print 'Case #' + str(tcNum+1) + ": " + str(x)

if(0):
  for _ in range(0,n):
    c = int(d[_*3+1])
    itms = [int(__) for __ in d[_*3+3].split(' ')]
    for a in range(0, len(itms)):
      for b in range(a+1, len(itms)):
        if(itms[a] + itms[b] == c):
          print 'Case #' + str(_+1) + ": " + str(a+1) + " " + str(b+1)
          break
if(0):
  st = [ord('a'), ord('d'), ord('g'), ord('j'), ord('m'), ord('p'), ord('t'), ord('w')]
  for tcNum in range(0,n):
    msg = d[tcNum+1].lower()
    dcd = ''
    for _ in msg:
      ch = _
      repeat = 1
      if(_ == ' '):
        ch = '0'
        repeat = 1
      else:
        a = -1
        for __ in range(len(st)):
          if(ord(_) >= st[__]):
            a = a + 1
          else:
            break
        ch = str(a+2)
        repeat = ord(_) - st[a] + 1
      if(len(dcd) > 0):
        if(dcd[-1] == ch):
          dcd =dcd + ' '
      for i in range(repeat):
        dcd = dcd + ch
    print 'Case #' + str(tcNum+1) + ": " + dcd