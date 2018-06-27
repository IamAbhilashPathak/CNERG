import sys
import os
import re
from math import log

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_QoE_metrics_new.txt"%(vid, mode))
input_filename1 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddown.log"%(vid, mode))
input_filename2 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddownload.txt"%(vid, mode))
input_filename3 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_rebuffer.txt"%(vid, mode))
input_filename4 = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed3.log"%(vid, mode))

bitrate_list = []
term1 = 0.0
term2 = 0.0
term3 = 0.0

with open(input_filename1, "r") as data:
 line_regex = re.compile("bandwidth\":([0-9]*?),")
 for line in data:
     a = line_regex.findall(line)
     for i in a:
	 bitrate_list.append(float(i)/1000)
     break

Q = []
R = []

with open(input_filename2, "r") as data:
  for line in data:
      p = line.split()
      Q.append(int(p[0]))

for i in Q:
  R.append(float(bitrate_list[i]))

for i in R:
  term1 += i
AVQ = term1/len(R)

for i in range(len(R)-1):
  term3 += abs(R[i+1]-R[i])
AQV = term3/(len(R)-1)

with open(input_filename3, "r") as data:
  for line in data:
      p = line.split()
      if (float(p[0]) > float(p[1])):
          term2 += float(p[0]) - float(p[1])
Rebuffer = term2

with open(input_filename4, "r") as data:
  line_regex = re.compile("\[([0-9]*?)\] N")
  line = data.readline()
  a = line_regex.search(line).group(1)
  Startup_Delay = float(a)/1000

with open(output_filename, "w") as out_file:
  out_file.write ("%f %f %f %f" % (AVQ,AQV,Rebuffer,Startup_Delay))

print AVQ,AQV,Rebuffer,Startup_Delay
