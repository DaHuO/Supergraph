#!/usr/bin/env python

import sys

def grupos(apilacion):
  if apilacion == ():
    return 0
  pan = apilacion[0]
  for i in xrange(1, len(apilacion)):
    if apilacion[i] != pan:
      return 1 + grupos(apilacion[i:])
  return 1

def vueltas(apilacion):
  cantidad_vueltas = grupos(apilacion)
  if apilacion[len(apilacion)-1]:
    cantidad_vueltas -= 1

  return cantidad_vueltas

if __name__ == '__main__':
  T = int(sys.stdin.readline())

  for i in xrange(T):
    apilacion = tuple(car == "+" for car in [p for p in sys.stdin.readline() if p in ('-', '+')])
    print "Case #%d: %s" % (i + 1, vueltas(apilacion))