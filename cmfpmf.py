import collections as cl
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def getPMF(x):
    x = [y for y in x]
    freq = cl.Counter(x).items()
    elements = zip(*freq)
    s = sum(elements[1])
    pdf = [(k[0],float(k[1])/s) for k in freq]
    # pdf.sort
    return pdf


def getCMF(elements):
    x = [y for y in elements]
    freq = cl.Counter(x).items()
    freq.sort(key = lambda x:x[0])
    x,y = zip(*freq)
    s = sum(y)
    cmf = [(p, float(sum(y[:i+1]))/s) for i, p in enumerate(x)]
    return cmf

http_qoe1 = []
quic_qoe1 = []
http_qoe2 = []
quic_qoe2 = []

count = 0

with open("QOE_metrics1", "r") as data:
    for line in data:
        p = line.split()
        if (count == 0):
           http_qoe1.append(float(p[0]))
           http_qoe2.append(float(p[1]))
        else:
           quic_qoe1.append(float(p[0]))
           quic_qoe2.append(float(p[1]))
        count = (count + 1) % 2

#x=[6,2,3,4,8,6,7,8,9,10]

w = getCMF(http_qoe1)
x = getCMF(quic_qoe1)
y = getCMF(http_qoe2)
z = getCMF(quic_qoe2)

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []

for i in w :
    a.append(i[0])
    b.append(i[1])
    #print i

for i in x :
    c.append(i[0])
    d.append(i[1])
    #print i

for i in y :
    e.append(i[0])
    f.append(i[1])
    #print i

for i in z :
    g.append(i[0])
    h.append(i[1])
    #print i

fig, ax = plt.subplots()
ax.set_xlabel('QoE')
ax.set_ylabel('CDF')
ax.plot(a,b,label='HTTP_QoE_lin')
ax.plot(c,d,label='QUIC_QoE_lin')
ax.plot(e,f,label='HTTP_QoE_log')
ax.plot(g,h,label='QUIC_QoE_log')


legend = ax.legend(loc=9)
plt.savefig('QOE.png')
plt.show()



