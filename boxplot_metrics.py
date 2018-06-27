import collections as cl
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

http = []
quic = []


x = ["http","quic"]
y = [http,quic]
count = 0

with open("QOE_metrics_new", "r") as data:
    for line in data:
        p = line.split()
        if (count == 0):
           http.append(float(p[3]))
        else:
           quic.append(float(p[3]))
        count = (count + 1) % 2

plt.ylabel('Startup Delay (in sec)')
plt.savefig('Startup Delay Boxplot.png')
plt.boxplot(y,labels = x)
plt.show()



