import sys
import os
import re
from math import log

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_QoE_metrics.txt"%(vid, mode))
input_filename1 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddown.log"%(vid, mode))
input_filename2 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddownload.txt"%(vid, mode))
input_filename3 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_rebuffer.txt"%(vid, mode))

bitrate_list = []
rebuffer_penalty_lin = 4.3
rebuffer_penalty_log = 2.66
term11 = 0.0
term12 = 0.0
term13 = 0.0
term21 = 0.0
term22 = 0.0
term23 = 0.0

with open(input_filename1, "r") as data:
 line_regex = re.compile("bandwidth\":([0-9]*?),")
 for line in data:
     a = line_regex.findall(line)
     for i in a:
	 bitrate_list.append(float(i)/1000000)
     break

R_min = bitrate_list[0]

with open(input_filename3, "r") as data:
  for line in data:
      p = line.split()
      if (float(p[0]) > float(p[1])):
          term12 += float(p[0]) - float(p[1])

term22 = term12

Q = []
R = []

with open(input_filename2, "r") as data:
  for line in data:
      p = line.split()
      Q.append(int(p[0]))

for i in Q:
  R.append(float(bitrate_list[i]))

for i in R:
  term11 += i
  term21 += log(i/R_min)

for i in range(len(R)-1):
  term13 += abs(R[i+1]-R[i])
  term23 += abs(log(R[i+1]/R_min) - log(R[i]/R_min))
 
QOE1 = term11 - (rebuffer_penalty_lin * term12) - term13
QOE2 = term21 - (rebuffer_penalty_log * term22) - term23

with open(output_filename, "w") as out_file:
  out_file.write ("%f %f" % (QOE1,QOE2))

#print term1,term2,term3
print QOE1,QOE2
