#!/usr/bin/env python3

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for tc in range(1, int(input())+1):
  sol = ''
  N = int(input())
  P = [int(x) for x in input().split()]
  tot = sum(P)
  flag = [False]*26

  m = 0
  while True:
    m = 0
    tmp = ''
    flag = [False]*26
    f1 = True
    for i in range(len(P)):
      if P[i] != 1:
        f1 = False
        break
    if f1:
      tmp1 = ''
      for i in range(len(P)):
        if P[i]==1:
          tmp1 += alpha[i]
      if len(tmp1) % 2 == 0:
        for i in range(0, len(tmp1), 2):
          tmp += tmp1[i]
          tmp += tmp1[i+1]
          if i+2 != len(tmp1):
            tmp += ' '
      else:
        tmp += tmp1[0]
        tmp += ' '
        for i in range(1, len(tmp1), 2):
          tmp += tmp1[i]
          tmp += tmp1[i+1]
          if i+2 != len(tmp1):
            tmp += ' '
    else:
      for i in range(len(P)):
        if P[i]>m and tmp == '':
          m = P[i]
          flag[i] = True
          tmp = alpha[i]
        elif P[i] >  m:
          for j in range(len(tmp)):
            flag[alpha.index(tmp[j])] = False
          tmp = alpha[i]
          flag[i] = True
          m = P[i]
        elif P[i]==m and m != 0:
          tmp += alpha[i]
          flag[i] = True
          m = P[i]
        if len(tmp)>2:
          flag[alpha.index(tmp[0])] = False
          tmp = tmp[1:]

    if len(tmp)==0:
      break
    if sol=='':
      sol += tmp
    else:
      sol += ' '
      sol += tmp
    for i in range(len(P)):
      if flag[i]:
        P[i] -= 1
    if f1:
      break

  print('Case #{_tc}: {_sol}'.format(_tc=tc, _sol=sol))

