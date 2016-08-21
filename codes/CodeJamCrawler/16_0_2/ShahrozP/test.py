def flip_cakes(cakes):
  if len(cakes) == 1:
    if cakes=='-':
      cakes='+'
      return 1;
    else:
      return 0;
  else:
    new_pile=""
    if cakes[-1] == '-':
      for cake in cakes:
        if cake=='-':
          new_pile += '+'
        else:
          new_pile+='-'
      return 1 + flip_cakes(new_pile[:-1])

    else:
      return flip_cakes(cakes[:-1])

           
t = int(raw_input()) 
for i in range(1, t + 1):
  total_cakes = raw_input() 
  print "Case #{}: {}".format(i, flip_cakes(total_cakes))