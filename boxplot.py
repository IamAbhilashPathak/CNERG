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

http_qoe1 = []
quic_qoe1 = []
http_qoe2 = []
quic_qoe2 = []

x = ["http_QoE_lin","quic_QoE_lin","http_QoE_log","quic_QoE_log"]
y = [http_qoe1,quic_qoe1,http_qoe2,quic_qoe2]
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

plt.ylabel('QOE')
plt.savefig('QOE_boxplot.png')
plt.boxplot(y,labels = x)
plt.show()



