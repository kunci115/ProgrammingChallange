# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:58:10 2016

@author: Rino Alfian - rino.alpin@gmail.com
"""
import sys
#soal 3n+1
#solved
n = raw_input().strip().split()
a = n[0]
b=n[1]
c = int(a)
d = int(b)
n = []
print c,d,
def loop():
    for i in range(c,d+1):
        counter = 1
        #print ""
        #print "Cycle Length ke ", i, ": ",
        g = i
        while g != 1:
            if g % 2 == 0:
                g = g / 2
            else:
                g = g*3+1
            counter = counter +1
            
        n.append(counter)    
        #print counter
        
        
    print max(n)
    return 0
loop()
