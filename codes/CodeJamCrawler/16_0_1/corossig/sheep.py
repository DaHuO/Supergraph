#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for caseno, line in enumerate(open("test.in", "r").readlines()[1:]) :
    number=int(line[:-1])
    found=[0] * 10
    nb_found=0
    msg="INSOMNIA"

    for i in range(1, 1000) :
        count = i*number

        while count > 0 and nb_found < 10 :
            digit=int(count%10)
            if found[digit] == 0 :
                found[digit] = 1
                nb_found+=1
            count = int(count/10)
            if nb_found == 10 :
                msg = str(i*number)

        if nb_found == 10 :
            break

    print("Case #%d: %s" % (caseno+1, msg))
