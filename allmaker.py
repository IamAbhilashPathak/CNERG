import sys
import os

output_filename = os.path.normpath("all.sh")

with open(output_filename, "w") as out_file:
    with open("times") as data:
         x = []
         y = []
         for line in data:
             p = line.split()
             x.append(p[0])
             y.append(p[1])
         length = len(x)

         out_file.write ("#!/bin/bash\n")
         for i in range(length):
             out_file.write ("python ~/Downloads/runTest.py" + " " + x[i] + " " + y[i] + " " + "http" + " " + "~/Downloads/trace.txt" + "\n")
             out_file.write ("python ~/Downloads/runTest.py" + " " + x[i] + " " + y[i] + " " + "quic" + " " + "~/Downloads/trace.txt" + "\n")
 
