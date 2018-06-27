import collections as cl
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def getCMF(elements):
    x = [y for y in elements]
    freq = cl.Counter(x).items()
    freq.sort(key = lambda x:x[0])
    x,y = zip(*freq)
    s = sum(y)
    cmf = [(p, float(sum(y[:i+1]))/s) for i, p in enumerate(x)]
    return cmf

http = []
quic = []

count = 0

with open("QOE_metrics_new", "r") as data:
    for line in data:
        p = line.split()
        if (count == 0):
           http.append(float(p[0]))
        else:
           quic.append(float(p[0]))
        count = (count + 1) % 2


w = getCMF(http)
x = getCMF(quic)

a = []
b = []
c = []
d = []

for i in w :
    a.append(i[0])
    b.append(i[1])
    #print i

for i in x :
    c.append(i[0])
    d.append(i[1])
    #print i

fig, ax = plt.subplots()
ax.set_xlabel('Average Video Quality (in kbps)')
ax.set_ylabel('CDF')
ax.plot(a,b,label='HTTP')
ax.plot(c,d,label='QUIC')

legend = ax.legend(loc=7)
plt.savefig('Average Video Quality.png')
plt.show()



